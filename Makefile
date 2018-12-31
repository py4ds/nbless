ENV_TOOL=pipenv
PYTHON=.venv/bin/python3
TESTER=pytest
LINTER=black

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
env: .venv/bin/activate

.venv/bin/activate: setup.py
ifneq ($(ENV_TOOL), venv)
	pip install $(ENV_TOOL)
endif
ifeq ($(ENV_TOOL), $(filter $(ENV_TOOL),virtualenv venv))
	test -d .venv || python -m $(ENV_TOOL) .venv
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --editable .
endif
ifeq ($(ENV_TOOL), pipenv)
	export PIPENV_VENV_IN_PROJECT=1
	test -d .venv || pipenv --three
	pipenv install pip
	pipenv install --editable .
endif

test: env
	pip install $(TESTER)
	${PYTHON} -m $(TESTER)

lint: env
	pip install $(LINTER)
	${PYTHON} -m $(LINTER)

.PHONY: env test lint