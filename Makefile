PYTHON ?= python3.14
VENV ?= .venv
VENV_PYTHON := $(VENV)/bin/python

.PHONY: setup preflight test agent-verify

setup:
	@command -v "$(PYTHON)" >/dev/null 2>&1 || (echo "$(PYTHON) が見つかりません。Python 3.14 を用意してください。" >&2; exit 1)
	"$(PYTHON)" -m venv "$(VENV)"
	"$(VENV_PYTHON)" -m pip install -r requirements.txt

preflight:
	"$(VENV_PYTHON)" tools/preflight.py

test:
	"$(VENV_PYTHON)" -m unittest discover -s tests -v

# issue契約・KB検証・生成物整合性をまとめた読み取り専用の統合ゲート。
agent-verify:
	@if test -x "$(VENV_PYTHON)" && test -f tools/agent_verify.py; then \
		if test -n "$(ISSUE)" && test -n "$(ISSUE_BODY)"; then echo "ISSUE と ISSUE_BODY は同時指定できません" >&2; exit 3; fi; \
		if test -z "$(NOW)"; then echo "NOW=YYYY-MM-DD が必要です" >&2; exit 3; fi; \
		args="--now $(NOW) $(ARGS)"; \
		if test -n "$(ISSUE)"; then args="--issue $(ISSUE) $$args"; \
		elif test -n "$(ISSUE_BODY)"; then args="--issue-body $(ISSUE_BODY) $$args"; \
		else echo "ISSUE または ISSUE_BODY が必要です" >&2; exit 3; fi; \
		"$(VENV_PYTHON)" tools/agent_verify.py $$args; \
	else \
		echo "agent-verify の実行環境がありません。先に make setup を実行してください。" >&2; \
		exit 3; \
	fi
