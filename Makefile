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

# #82で実装する統合ゲートの予約入口。未実装期間も、誤って成功扱いにしない。
agent-verify:
	@if test -x "$(VENV_PYTHON)" && test -f tools/agent_verify.py; then \
		"$(VENV_PYTHON)" tools/agent_verify.py $(ARGS); \
	else \
		echo "agent-verify は #82 の実装後に利用できます。" >&2; \
		exit 3; \
	fi
