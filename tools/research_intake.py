#!/usr/bin/env python3
"""Versioned social observations, validated by native KB rules, in owner Git."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
import yaml

try:
    from .kb import ROOT, DIR_FOR_TYPE, load_config, recheck_deadline
    from .build_graph import validate as validate_native
    from .export_signals import build_record, _head_commit
except ImportError:
    from kb import ROOT, DIR_FOR_TYPE, load_config, recheck_deadline
    from build_graph import validate as validate_native
    from export_signals import build_record, _head_commit

CONTRACT = 'market-observation/v1'
POLICY = 'market-observation-policy/v1'
OWNER = 'marketing-trends-notes'
REF = 'refs/heads/knowledge'
SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
SHA = re.compile(r'^[0-9a-f]{40}$')
FIELDS = set('contract_version record_id revision creator_id origin_instance_id collection_id observed_at epistemic_status lifecycle document reference_documents source_checks supersedes'.split())

class IntakeError(ValueError):
    pass

def need(value, reason):
    if not value:
        raise IntakeError(reason)

def data(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))+'\n').encode()

def digest(value):
    return hashlib.sha256(value).hexdigest()

def git(root, *args, content=None, env=None):
    result = subprocess.run(['git','-C',str(root),*args],input=content,capture_output=True,env=env)
    need(result.returncode == 0, 'GIT_FAILED')
    return result.stdout.decode().strip()

def timestamp(value):
    try:
        stamp=datetime.fromisoformat(value.replace('Z','+00:00'))
        need(stamp.tzinfo is not None,'TIMEZONE_REQUIRED')
        return stamp
    except (ValueError,TypeError,AttributeError):
        raise IntakeError('TIMESTAMP_INVALID') from None

def safe_root(value):
    root=Path(value)
    need(root.is_absolute() and not any(p.is_symlink() for p in [root,*root.parents]),'STORE_PATH_INVALID')
    root=root.resolve()
    need(not root.is_relative_to(ROOT) and not ROOT.is_relative_to(root),'STORE_CODE_OVERLAP')
    return root

def write_commit(root, parent, updates):
    with tempfile.TemporaryDirectory(prefix='market-index-') as directory:
        env=dict(os.environ,GIT_INDEX_FILE=str(Path(directory)/'index'),GIT_AUTHOR_NAME='Market observation',GIT_AUTHOR_EMAIL='memory@localhost',GIT_COMMITTER_NAME='Market observation',GIT_COMMITTER_EMAIL='memory@localhost')
        git(root,'read-tree',parent if parent else '--empty',env=env)
        for name,value in sorted(updates.items()):
            blob=git(root,'hash-object','-w','--stdin',content=value,env=env)
            git(root,'update-index','--add','--cacheinfo',f'100644,{blob},{name}',env=env)
        tree=git(root,'write-tree',env=env)
        commit=git(root,'commit-tree',tree,*(['-p',parent] if parent else []),'-m','Persist validated market observation',env=env)
        result=subprocess.run(['git','-C',str(root),'update-ref',REF,commit,parent or '0'*40],capture_output=True)
        need(result.returncode==0,'PARENT_CONFLICT')
        need(git(root,'rev-parse',f'{commit}^{{tree}}')==tree,'COMMIT_VERIFICATION_FAILED')
        return commit

def init(root, *, creator, instance, collection):
    root=safe_root(root)
    for item in (creator,instance,collection): need(isinstance(item,str) and SLUG.fullmatch(item),'IDENTITY_INVALID')
    need(not root.exists(),'STORE_EXISTS')
    root.mkdir(parents=True);git(root,'init','--bare','--quiet');git(root,'symbolic-ref','HEAD',REF)
    identity=dict(contract_version='market-knowledge-store/v1',owner=OWNER,creator_id=creator,origin_instance_id=instance,collection_id=collection)
    commit=write_commit(root,None,{'entities/observation-history/store.json':data(identity)})
    return {'status':'COMMITTED','target_commit':commit}

def open_store(root, *, creator, collection, snapshot=None):
    root=safe_root(root)
    need(git(root,'rev-parse','--is-bare-repository')=='true','BARE_STORE_REQUIRED')
    current=git(root,'rev-parse',REF)
    commit=snapshot or current
    need(isinstance(commit,str) and SHA.fullmatch(commit),'SNAPSHOT_INVALID')
    git(root,'merge-base','--is-ancestor',commit,current)
    tree={}
    for line in git(root,'ls-tree','-r',commit).splitlines():
        info,name=line.split('\t',1)
        need(info.startswith('100644 blob '),'STORE_ENTRY_INVALID')
        need(bool(re.fullmatch(r'entities/observation-history/(store\.json|(?:records|operations)/[a-z0-9-]+/[1-9][0-9]*\.json)',name)),'STORE_PATH_INVALID')
        tree[name]=json.loads(git(root,'show',f'{commit}:{name}'))
    identity=tree.get('entities/observation-history/store.json',{})
    need(identity.get('contract_version')=='market-knowledge-store/v1' and identity.get('owner')==OWNER,'STORE_SCHEMA_INVALID')
    need((creator,collection)==(identity.get('creator_id'),identity.get('collection_id')),'STORE_SCOPE_MISMATCH')
    return root,commit,tree,identity

def document(value):
    need(isinstance(value,str) and value.startswith('---\n'),'FRONTMATTER_REQUIRED')
    try:
        _,header,body=value.split('---\n',2);meta=yaml.safe_load(header)
    except (ValueError,yaml.YAMLError):
        raise IntakeError('FRONTMATTER_INVALID') from None
    need(isinstance(meta,dict),'FRONTMATTER_INVALID')
    need(not re.search(r'ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]+|-----BEGIN .*PRIVATE KEY',value),'RESTRICTED_CONTENT')
    need(not any(key in meta for key in ('raw','raw_voice','credentials','token')),'RAW_FORBIDDEN')
    return meta,body

def source_url(value):
    need(isinstance(value,str),'SOURCE_INVALID')
    parsed=urlsplit(value)
    need(parsed.scheme in ('http','https') and parsed.hostname and not parsed.username and not parsed.password,'SOURCE_INVALID')
    return urlunsplit((parsed.scheme.lower(),parsed.netloc.lower(),parsed.path or '/',parsed.query,parsed.fragment))

def validate(record, identity, *, now):
    need(isinstance(record,dict) and set(record)==FIELDS,'RECORD_FIELDS_INVALID')
    need(record['contract_version']==CONTRACT,'RECORD_SCHEMA_INVALID')
    need(isinstance(record['record_id'],str) and SLUG.fullmatch(record['record_id']),'RECORD_ID_INVALID')
    need(type(record['revision']) is int and record['revision']>=1,'REVISION_INVALID')
    need(record['supersedes']==(record['revision']-1 if record['revision']>1 else None),'SUPERSESSION_INVALID')
    for key in ('creator_id','origin_instance_id','collection_id'): need(record[key]==identity[key],'CREATOR_SCOPE_MISMATCH')
    need(record['epistemic_status'] in ('observed','externally-supported','inferred','proposed','simulated','unknown'),'EPISTEMIC_INVALID')
    need(record['lifecycle'] in ('accepted','revoked'),'LIFECYCLE_INVALID')
    observed=timestamp(record['observed_at']);clock=timestamp(now)
    need(observed<=clock,'FUTURE_OBSERVATION')
    meta,body=document(record['document'])
    need(meta.get('type') in ('trend','practice','concept'),'KIND_NOT_SUPPORTED')
    need(isinstance(meta.get('id'),str) and re.fullmatch(r'(trend|practice|concept)/[a-z0-9]+(?:-[a-z0-9]+)*',meta['id']),'ENTITY_ID_INVALID')
    # Context candidates map to the native concept type; no ninth entity type.
    geo=meta.get('geo');channels=sorted(item['target'] for item in meta.get('channels',[]))
    need(geo in load_config()['geographies'],'GEO_REQUIRED')
    need(isinstance(meta.get('counterevidence'),list),'COUNTEREVIDENCE_REQUIRED')
    checks=record['source_checks'];need(isinstance(checks,list) and checks,'SOURCE_CHECKS_REQUIRED')
    by_source={}
    for check in checks:
        need(isinstance(check,dict) and set(check)=={'source','retrieved','checked_at','content_sha256','geo','channels'},'SOURCE_CHECK_FIELDS')
        url=source_url(check['source']);need(url not in by_source,'DUPLICATE_SOURCE_CHECK')
        need(check['retrieved'] in ('primary','summary'),'RETRIEVAL_INVALID')
        need(timestamp(check['checked_at'])<=observed,'UNOBSERVED_RECHECK')
        need(isinstance(check['content_sha256'],str) and re.fullmatch(r'[0-9a-f]{64}',check['content_sha256']),'SOURCE_HASH_REQUIRED')
        need(check['geo']==geo and sorted(check['channels'])==channels,'SOURCE_APPLICABILITY_MISMATCH')
        by_source[url]=check
    evidence=meta.get('evidence') or [];need(evidence,'EVIDENCE_REQUIRED')
    for item in evidence:
        url=source_url(item['source']);need(url in by_source,'SOURCE_NOT_CHECKED')
        need(item['retrieved']==by_source[url]['retrieved'],'UNREAD_PRIMARY')
        need(item['source'] in meta.get('sources',[]),'SOURCE_NOT_DECLARED')
        need(isinstance(item.get('as_of'),str) and bool(item['as_of']),'AS_OF_REQUIRED')
    if record['epistemic_status'] in ('observed','externally-supported'):
        need(any(e['retrieved']=='primary' and e['certainty'] in ('measured','independent','attested') for e in evidence),'UNSUPPORTED_EPISTEMIC_PROMOTION')
    fresh=meta.get('freshness') or {}
    if meta.get('type')=='trend' and meta.get('stage')!='dead':
        verified=fresh.get('valid_as_of');need(isinstance(verified,str),'FRESHNESS_REQUIRED')
        primary=[check for check in checks if check['retrieved']=='primary']
        need(not primary or all(timestamp(check['checked_at']).date().isoformat()>=verified for check in primary),'UNCONFIRMED_FRESHNESS')
        need(verified<=observed.date().isoformat(),'FUTURE_FRESHNESS')
    # Native validator checks vocabulary, verified evidence, freshness deadlines,
    # required body sections and references. Nothing promotes a draft to verified.
    path=ROOT/'entities'/DIR_FOR_TYPE[meta['type']]/(meta['id'].split('/')[1]+'.md')
    checked=dict(meta,path=str(path.relative_to(ROOT)))
    entities={meta['id']:checked}; native_records=[(path,checked,body)]
    need(isinstance(record['reference_documents'],list),'REFERENCE_DOCUMENTS_INVALID')
    for source_document in record['reference_documents']:
        ref,ref_body=document(source_document)
        need(ref.get('type') in DIR_FOR_TYPE and isinstance(ref.get('id'),str),'REFERENCE_INVALID')
        need(re.fullmatch(r'[a-z-]+/[a-z0-9]+(?:-[a-z0-9]+)*',ref['id']),'REFERENCE_ID_INVALID')
        need(ref['id'] not in entities,'REFERENCE_DUPLICATE')
        ref_path=ROOT/'entities'/DIR_FOR_TYPE[ref['type']]/(ref['id'].split('/')[1]+'.md')
        ref=dict(ref,path=str(ref_path.relative_to(ROOT)))
        entities[ref['id']]=ref;native_records.append((ref_path,ref,ref_body))
    errors=[];validate_native(entities,native_records,load_config(),errors)
    need(not errors,'NATIVE_SCHEMA_INVALID: '+ '; '.join(errors))
    return checked

def record_path(record):
    return f"entities/observation-history/records/{record['record_id']}/{record['revision']}.json"

def latest(tree):
    result={}
    rows=[(name,value) for name,value in tree.items() if '/records/' in name]
    for name,record in sorted(rows,key=lambda row:(row[0].split('/')[-2],int(row[0].split('/')[-1][:-5]))):
        need(name==record_path(record),'RECORD_PATH_MISMATCH')
        previous=result.get(record['record_id'])
        need(record['revision']==(previous['revision']+1 if previous else 1),'REVISION_GAP')
        result[record['record_id']]=record
    return result

def observation_key(record):
    meta,_=document(record['document'])
    # Source + claim field + source data time + applicability, independent of title/ID.
    return data([sorted((source_url(e['source']),e['field'],e['as_of']) for e in meta['evidence']),meta['geo'],sorted(c['target'] for c in meta.get('channels',[]))])

def index(root, *, creator, collection, now, snapshot=None):
    root,commit,tree,identity=open_store(root,creator=creator,collection=collection,snapshot=snapshot)
    records=[]
    for record in latest(tree).values():
        meta=validate(record,identity,now=now)
        signal=build_record(meta,_head_commit(),timestamp(now),'artistic-research')
        status=signal['freshness']['status'] if signal else 'unknown'
        if not any(c['retrieved']=='primary' for c in record['source_checks']):status='unknown'
        if record['lifecycle']=='revoked':status='revoked'
        records.append({'record_id':record['record_id'],'revision':record['revision'],'payload_ref':record_path(record),'content_sha256':digest(data(record)), 'freshness':status,'geo':meta['geo'],'channels':sorted(c['target'] for c in meta.get('channels',[])), 'as_of':sorted({e['as_of'] for e in meta['evidence']})})
    result={'contract_version':'market-observation-index/v1','knowledge_commit':commit,'now':now,'records':records}
    path=root/'observation-index.json';need(not path.is_symlink(),'INDEX_PATH_INVALID')
    with tempfile.NamedTemporaryFile(dir=root,delete=False) as handle:
        handle.write(data(result));temporary=Path(handle.name)
    os.replace(temporary,path)
    return result

def receipt(root, stored, *, creator, collection, now, status):
    commits=git(root,'rev-list','--reverse',REF,'--',stored['operation_path']).splitlines();need(commits,'RECEIPT_MISSING')
    result=dict(contract_version='knowledge-write-receipt/v1',operation_id=stored['operation_id'],run_id=stored['run_id'],owner=OWNER,collection=collection,target_parent=stored['parent'],target_commit=commits[0],accepted_ids=[stored['record_id']],rejected_ids=[],schema_version=CONTRACT,policy_version=POLICY,index_commit=None,index_hash=None,status=status,reason='ALREADY_APPLIED' if status=='NO_CHANGE' else 'VALIDATED')
    try:
        indexed=index(root,creator=creator,collection=collection,now=now)
        result.update(index_commit=indexed['knowledge_commit'],index_hash=digest(data(indexed)))
    except (ValueError,OSError):result.update(status='INDEX_PENDING',reason='knowledge retained; retry index')
    return result

def commit(root, record, *, creator, collection, now, expected_parent, operation_id, run_id):
    root,parent,tree,identity=open_store(root,creator=creator,collection=collection)
    for value in (operation_id,run_id):need(isinstance(value,str) and SLUG.fullmatch(value),'OPERATION_ID_INVALID')
    path=f'entities/observation-history/operations/{operation_id}/1.json';content_hash=digest(data(record))
    existing=tree.get(path)
    if existing:
        need(existing['hash']==content_hash and existing['run_id']==run_id,'OPERATION_CONFLICT')
        return receipt(root,existing,creator=creator,collection=collection,now=now,status='NO_CHANGE')
    need(parent==expected_parent,'PARENT_CONFLICT')
    validate(record,identity,now=now); records=latest(tree);previous=records.get(record['record_id'])
    for old in (value for name,value in tree.items() if '/records/' in name):
        if observation_key(old)==observation_key(record) and old['record_id']!=record['record_id']:
            raise IntakeError('DUPLICATE_OBSERVATION')
    prior=tree.get(record_path(record))
    if prior:
        need(prior==record,'REVISION_CONFLICT')
        stored=next(v for k,v in tree.items() if '/operations/' in k and v['hash']==content_hash)
        return receipt(root,stored,creator=creator,collection=collection,now=now,status='NO_CHANGE')
    need(record['revision']==(previous['revision']+1 if previous else 1),'REVISION_CONFLICT')
    if previous:
        need(any(previous[k]!=record[k] for k in ('document','reference_documents','source_checks','epistemic_status','lifecycle')),'DUPLICATE_OBSERVATION')
        before,_=document(previous['document']);after,_=document(record['document'])
        need(before['id']==after['id'],'ENTITY_ID_CHANGED')
        need(timestamp(record['observed_at'])>=timestamp(previous['observed_at']),'OBSERVATION_TIME_REVERSED')
    stored=dict(contract_version='market-observation-operation/v1',operation_path=path,operation_id=operation_id,run_id=run_id,parent=parent,record_id=record['record_id'],hash=content_hash,code_commit=_head_commit())
    new=write_commit(root,parent,{record_path(record):data(record),path:data(stored)})
    need(json.loads(git(root,'show',f'{new}:{record_path(record)}'))==record,'COMMIT_VERIFICATION_FAILED')
    return receipt(root,stored,creator=creator,collection=collection,now=now,status='COMMITTED')

def retrieve(root, *, creator, collection, now, geo, channels, snapshot=None):
    root,snapshot,tree,identity=open_store(root,creator=creator,collection=collection,snapshot=snapshot)
    indexed=index(root,creator=creator,collection=collection,now=now,snapshot=snapshot)
    hits=[];revalidate=[]
    for item in indexed['records']:
        if item['geo']!=geo or sorted(channels)!=item['channels']:continue
        record=tree[item['payload_ref']]
        hits.append(dict(item,record=record,reason='Exact region/channel match; source dates retained'))
        if item['freshness']!='current':
            revalidate.append({'record_id':item['record_id'],'revision':item['revision'],'action':'reopen-primary-source','status':'PENDING','reason':item['freshness'],'budget_required':True})
    return {'status':'FOUND' if hits else ('EMPTY_HISTORY' if not indexed['records'] else 'NOT_APPLICABLE'),'knowledge_commit':snapshot,'records':hits,'revalidation_tasks':revalidate}

def artifact_record(record, knowledge_commit, code_commit):
    meta,_=document(record['document'])
    until=(meta.get('freshness') or {}).get('recheck_by')
    return dict(contract_version='artifact-record/v1',record_id=record['record_id'],revision=record['revision'],
                origin_instance_id=record['origin_instance_id'],creator_id=record['creator_id'],owner_repository=OWNER,
                collection_id=record['collection_id'],kind='market-observation',payload_schema=CONTRACT,
                payload_ref=record_path(record),content_sha256=digest(data(record)),
                sources=[dict(locator=c['source'],content_sha256=c['content_sha256'],retrieved=c['retrieved'],checked_at=c['checked_at']) for c in record['source_checks']],
                derived_from=[],epistemic_status=record['epistemic_status'],lifecycle=record['lifecycle'],
                applicability=dict(geo=meta['geo'],channels=meta.get('channels',[]),as_of=sorted({e['as_of'] for e in meta['evidence']})),
                rights=dict(policy='source-links-and-derived-notes-only',redistribution=False),access_scope='local',consent_ref=None,
                created_at=record['observed_at'],reviewed_at=None,valid_until=until+'T23:59:59+00:00' if until else None,
                producer=dict(kind='external-agent',generator_version=POLICY,code_commit=code_commit,knowledge_commit=knowledge_commit),
                supersedes=[] if record['supersedes'] is None else [dict(record_id=record['record_id'],revision=record['supersedes'])],
                invalidates=[] if record['lifecycle']!='revoked' or record['supersedes'] is None else [dict(record_id=record['record_id'],revision=record['supersedes'])])


def exchange(root, **options):
    root,snapshot,tree,identity=open_store(root,creator=options['creator'],collection=options['collection'],snapshot=options.get('snapshot'))
    records=[]
    for record in latest(tree).values():
        validate(record,identity,now=options['now'])
        records.append(artifact_record(record,snapshot,_head_commit()))
    return dict(contract_version='market-knowledge-exchange/v1',owner_repository=OWNER,knowledge_commit=snapshot,records=records)


def export(root, **options):
    found=retrieve(root,**options);now=timestamp(options['now']);code=_head_commit();signals=[]
    for hit in found['records']:
        if hit['freshness']=='revoked':continue
        meta=validate(hit['record'],dict(creator_id=options['creator'],collection_id=options['collection'],origin_instance_id=hit['record']['origin_instance_id']),now=options['now']);signal=build_record(meta,code,now,'artistic-research')
        if signal:
            signal['freshness']['status']=hit['freshness']
            if hit['freshness']=='unknown':
                signal['validity']['status']='unknown'
                signal['unknowns'].append('Primary source recheck unconfirmed; freshness remains unknown.')
            if hit['record']['epistemic_status'] in ('simulated','unknown','proposed','inferred'):
                signal['certainty']['level']='inferred'
                signal['constraints'].append('Epistemic status: '+hit['record']['epistemic_status'])
            signal['constraints']+=['Knowledge snapshot: '+found['knowledge_commit'], 'Source data dates (as_of): '+', '.join(hit['as_of']), 'Geography: '+hit['geo'], 'Popularity is not an artistic quality criterion.']
            signal['source_locator']=hit['payload_ref']
            signal['evidence_locator']=hit['payload_ref']+'#document.evidence'
            signals.append(signal)
    return {'contract_version':'research-signal-export/v1','source_repository':'marketing-trends','source_commit':code,'purpose':'artistic-research','generated_at':now.isoformat(timespec='seconds'),'signal_count':len(signals),'stale_count':sum(s['freshness']['status']=='stale' for s in signals),'signals':signals}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('command',choices=['init','prepare','validate','commit','index','retrieve','export','exchange','invalidate'])
    parser.add_argument('--store-root',type=Path,required=True);parser.add_argument('--creator',required=True);parser.add_argument('--collection',required=True);parser.add_argument('--instance');parser.add_argument('--now',required=True)
    parser.add_argument('--record',type=Path);parser.add_argument('--expected-parent');parser.add_argument('--operation-id');parser.add_argument('--run-id');parser.add_argument('--geo');parser.add_argument('--channel',action='append',default=[]);parser.add_argument('--snapshot')
    args=parser.parse_args();options=dict(creator=args.creator,collection=args.collection,now=args.now)
    try:
        if args.command=='init':result=init(args.store_root,creator=args.creator,collection=args.collection,instance=args.instance)
        elif args.command in ('prepare','validate','commit','invalidate'):
            need(args.record is not None and args.record.is_file() and not args.record.is_symlink(),'RECORD_REQUIRED');record=json.loads(args.record.read_text())
            if args.command=='invalidate':need(record.get('lifecycle')=='revoked','REVOCATION_REQUIRED')
            if args.command in ('commit','invalidate'):result=commit(args.store_root,record,**options,expected_parent=args.expected_parent,operation_id=args.operation_id,run_id=args.run_id)
            else:
                _,parent,_,identity=open_store(args.store_root,creator=args.creator,collection=args.collection);validate(record,identity,now=args.now);result={'status':'VALID','parent':parent,'content_sha256':digest(data(record))}
        elif args.command=='index':result=index(args.store_root,**options,snapshot=args.snapshot)
        elif args.command=='exchange':result=exchange(args.store_root,**options,snapshot=args.snapshot)
        elif args.command=='retrieve':result=retrieve(args.store_root,**options,geo=args.geo,channels=args.channel,snapshot=args.snapshot)
        else:result=export(args.store_root,**options,geo=args.geo,channels=args.channel,snapshot=args.snapshot)
        print(data(result).decode(),end='');return 0
    except IntakeError as exc:
        reason=str(exc).split(':',1)[0]
        print(json.dumps({'status':'CONFLICT' if reason.endswith('CONFLICT') else 'REJECTED','reason':reason}));return 2
    except (ValueError,OSError,KeyError,TypeError):
        print(json.dumps({'status':'REJECTED','reason':'MALFORMED_INPUT'}));return 2

if __name__=='__main__':raise SystemExit(main())
