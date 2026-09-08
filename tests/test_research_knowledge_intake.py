"""AAK07: real isolated Git persistence and native source/freshness boundaries."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import yaml

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import research_intake as intake

NOW='2026-09-05T12:00:00+00:00'
LATER='2026-11-06T12:00:00+00:00'
SOURCE='https://example.org/synthetic-observation'


def markdown(meta,body='## 反証\nSynthetic fixture: reversed participation would refute this observation.\n'):
    return '---\n'+yaml.safe_dump(meta,allow_unicode=True,sort_keys=False)+'---\n'+body


def candidate(revision=1,as_of='2026-08',checked='2026-09-05',retrieved='primary',certainty='independent',kind='trend'):
    meta=dict(id=kind+'/synthetic-observation',uri='urn:mtn:'+kind+'/synthetic-observation',type=kind,label_ja='合成観測',label_en='Synthetic observation',sources=[SOURCE],status='draft',updated=checked,authority={'none_reason':'Synthetic fixture; no real authority asserted.'},geo='japan',channels=[{'target':'channel/synthetic-channel','role':'originated_on'}],counterevidence=['A reversed synthetic count would refute the claim.'],relations=[],evidence=[dict(field=field,source=SOURCE,certainty=certainty,retrieved=retrieved,as_of=as_of) for field in ('kind','stage','time')])
    body='## 反証\nSynthetic evidence only; no real observation or source access claimed.\n'
    if kind=='trend':
        meta.update(kind='demand-shift',stage='emerging',market='cross-category',naming={'self_identified':False,'note':'Synthetic description'},channel_scope={'status':'mapped','note':None},freshness={'valid_as_of':checked,'recheck_by':intake.recheck_deadline('emerging',checked)})
    elif kind=='practice':
        from build_graph import PRACTICE_HEADINGS
        body='\n'.join(heading+'\nSynthetic; effect unconfirmed.' for heading in PRACTICE_HEADINGS)
    channel=dict(id='channel/synthetic-channel',uri='urn:mtn:channel/synthetic-channel',type='channel',label_ja='合成チャネル',sources=[SOURCE],status='draft',updated=checked,authority={'none_reason':'Synthetic fixture'},relations=[])
    return dict(contract_version=intake.CONTRACT,record_id='synthetic-observation',revision=revision,creator_id='synthetic-creator',origin_instance_id='synthetic-instance',collection_id='synthetic-collection',observed_at=checked+'T12:00:00+00:00',epistemic_status='simulated',lifecycle='accepted',document=markdown(meta,body),reference_documents=[markdown(channel,'Synthetic reference definition only.')],source_checks=[dict(source=SOURCE,retrieved=retrieved,checked_at=checked+'T10:00:00+00:00',content_sha256='a'*64,geo='japan',channels=['channel/synthetic-channel'])],supersedes=revision-1 if revision>1 else None)


class ResearchKnowledgeIntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(dir='/private/tmp')
        self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'memory.git'
        self.options=dict(creator='synthetic-creator',collection='synthetic-collection',now=NOW)
        self.initial=intake.init(self.root,creator=self.options['creator'],instance='synthetic-instance',collection=self.options['collection'])['target_commit']

    def save(self,record=None,operation='first',now=NOW,parent=None):
        return intake.commit(self.root,record or candidate(),**dict(self.options,now=now),expected_parent=parent or intake.git(self.root,'rev-parse',intake.REF),operation_id=operation,run_id='synthetic-run')

    def get(self,now=NOW,**extra):
        return intake.retrieve(self.root,**dict(self.options,now=now),geo=extra.pop('geo','japan'),channels=extra.pop('channels',['channel/synthetic-channel']),**extra)

    def test_ac1_duplicate_and_historical_source_dates_survive_restart(self):
        first=self.save();repeat=self.save()
        self.assertEqual(repeat['status'],'NO_CHANGE');self.assertEqual(first['target_commit'],repeat['target_commit'])
        duplicate=candidate();duplicate['record_id']='renamed-observation'
        with self.assertRaisesRegex(intake.IntakeError,'DUPLICATE_OBSERVATION'): self.save(duplicate,'renamed')
        second=self.save(candidate(2,'2026-10','2026-11-06'),'second',LATER)
        self.assertNotEqual(first['target_commit'],second['target_commit'])
        (self.root/'observation-index.json').unlink()
        args=[sys.executable,str(intake.ROOT/'tools/research_intake.py'),'retrieve','--store-root',str(self.root),'--creator',self.options['creator'],'--collection',self.options['collection'],'--now',LATER,'--geo','japan','--channel','channel/synthetic-channel']
        output=subprocess.run(args,capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(output.stdout)['records'][0]['as_of'],['2026-10'])
        old=self.get(now=LATER,snapshot=first['target_commit'])['records'][0]
        self.assertEqual(old['as_of'],['2026-08']);self.assertEqual(old['freshness'],'stale')

    def test_ac2_clock_expiry_and_real_recheck_required(self):
        self.save();self.assertEqual(self.get()['records'][0]['freshness'],'current')
        expired=self.get(LATER);self.assertEqual(expired['records'][0]['freshness'],'stale')
        self.assertEqual(expired['revalidation_tasks'][0]['status'],'PENDING')
        invented=candidate(2,'2026-10','2026-11-06');invented['source_checks'][0]['checked_at']='2026-09-05T10:00:00+00:00'
        with self.assertRaisesRegex(intake.IntakeError,'UNCONFIRMED_FRESHNESS'):self.save(invented,'invented',LATER)
        self.assertEqual(self.get(LATER)['records'][0]['freshness'],'stale')
        self.save(candidate(2,'2026-10','2026-11-06'),'rechecked',LATER)
        self.assertEqual(self.get(LATER)['records'][0]['freshness'],'current')

    def test_ac3_geography_channel_and_vendor_verified_rejected(self):
        self.save();self.assertEqual(self.get(geo='us')['status'],'NOT_APPLICABLE')
        self.assertEqual(self.get(channels=['channel/another'])['status'],'NOT_APPLICABLE')
        for field,value in [('geo','us'),('channels',['channel/another'])]:
            bad=candidate(2);bad['source_checks'][0][field]=value
            with self.assertRaisesRegex(intake.IntakeError,'SOURCE_APPLICABILITY_MISMATCH'):self.save(bad,'bad-'+field)
        bad=candidate(2,certainty='vendor');meta,body=intake.document(bad['document']);meta['status']='verified';bad['document']=markdown(meta,body)
        with self.assertRaisesRegex(intake.IntakeError,'NATIVE_SCHEMA_INVALID'):self.save(bad,'vendor')

    def test_ac4_second_export_has_new_observation_and_separate_knowledge_pin(self):
        first=self.save();self.save(candidate(2,'2026-10','2026-11-06'),'second',LATER)
        result=intake.export(self.root,**dict(self.options,now=LATER),geo='japan',channels=['channel/synthetic-channel'])
        self.assertEqual(result['signal_count'],1);signal=result['signals'][0]
        self.assertIn('2026-10',' '.join(signal['constraints']));self.assertNotIn('2026-08',' '.join(signal['constraints']))
        self.assertEqual(signal['freshness']['status'],'current');self.assertTrue(signal['source_locator'].endswith('/2.json'))
        self.assertIn('Popularity is not an artistic quality criterion.',signal['constraints'])
        old=intake.export(self.root,**dict(self.options,now=LATER),geo='japan',channels=['channel/synthetic-channel'],snapshot=first['target_commit'])
        self.assertEqual(old['signals'][0]['freshness']['status'],'stale')

    def test_cas_revision_operation_conflicts_preserve_success(self):
        first=self.save()
        for record,op,parent,reason in [(candidate(2),'second',self.initial,'PARENT_CONFLICT'),(candidate(3),'gap',first['target_commit'],'REVISION_CONFLICT'),(candidate(2),'first',first['target_commit'],'OPERATION_CONFLICT')]:
            with self.assertRaisesRegex(intake.IntakeError,reason):self.save(record,op,parent=parent)
        self.assertEqual(intake.git(self.root,'rev-parse',intake.REF),first['target_commit'])

    def test_index_failure_keeps_receipt_and_resumes(self):
        with patch.object(intake,'index',side_effect=OSError('synthetic index failure')):receipt=self.save()
        self.assertEqual(receipt['status'],'INDEX_PENDING')
        resumed=self.save();self.assertEqual(resumed['status'],'NO_CHANGE');self.assertEqual(resumed['target_commit'],receipt['target_commit'])
        self.assertIsNotNone(resumed['index_hash']);self.assertEqual(len(self.get()['records']),1)

    def test_unknown_context_and_native_practice_are_retained(self):
        for kind in ('concept','practice'):
            record=candidate(kind=kind,retrieved='summary',certainty='hypothesis');record['record_id']=kind+'-observation'
            # Different source data observations avoid claiming distinct titles as new knowledge.
            meta,body=intake.document(record['document'])
            for evidence in meta['evidence']:evidence['as_of']='2026-07' if kind=='concept' else '2026-06'
            record['document']=markdown(meta,body);self.save(record,kind)
        found=self.get();self.assertEqual(len(found['records']),2)
        self.assertTrue(all(row['freshness']=='unknown' for row in found['records']))
        self.assertEqual(len(found['revalidation_tasks']),2)

    def test_missing_reference_unread_primary_and_creator_mismatch_rejected(self):
        bad=candidate();bad['reference_documents']=[]
        with self.assertRaisesRegex(intake.IntakeError,'NATIVE_SCHEMA_INVALID'):self.save(bad)
        bad=candidate();bad['source_checks'][0]['retrieved']='summary'
        with self.assertRaisesRegex(intake.IntakeError,'UNREAD_PRIMARY'):self.save(bad)
        bad=candidate();bad['creator_id']='other-creator'
        with self.assertRaisesRegex(intake.IntakeError,'CREATOR_SCOPE_MISMATCH'):self.save(bad)
        self.assertEqual(self.get()['status'],'EMPTY_HISTORY')

    def test_source_correction_revocation_and_native_export_cli(self):
        first=self.save()
        args=[sys.executable,str(intake.ROOT/'tools/export_signals.py'),'--purpose','artistic-research','--knowledge-store',str(self.root),'--creator',self.options['creator'],'--collection',self.options['collection'],'--geo','japan','--channel','channel/synthetic-channel','--now',NOW]
        result=subprocess.run(args,capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)['signal_count'],1)
        revoked=candidate(2);revoked['lifecycle']='revoked'
        self.save(revoked,'revoke')
        result=subprocess.run(args,capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)['signal_count'],0)
        exchanged=intake.exchange(self.root,**self.options)
        record=exchanged['records'][0]
        self.assertEqual(record['invalidates'],[{'record_id':'synthetic-observation','revision':1}])
        self.assertEqual(record['epistemic_status'],'simulated')
        self.assertEqual(self.get(snapshot=first['target_commit'])['records'][0]['record']['lifecycle'],'accepted')

    def test_summary_trend_stays_unknown_and_old_duplicate_stays_rejected(self):
        self.save(candidate(retrieved='summary',certainty='hypothesis'))
        self.assertEqual(self.get()['records'][0]['freshness'],'unknown')
        self.save(candidate(2,'2026-10','2026-11-06'),'second',LATER)
        duplicate=candidate(retrieved='summary',certainty='hypothesis');duplicate['record_id']='different-title'
        with self.assertRaisesRegex(intake.IntakeError,'DUPLICATE_OBSERVATION'):self.save(duplicate,'old-duplicate',LATER)

if __name__=='__main__':unittest.main()
