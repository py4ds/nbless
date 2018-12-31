# If ENV is pipenv, run export PIPENV_VENV_IN_PROJECT=1
# Otherwise, .venv will not be in the current project.

ENV=virtualenv
PYTHON=.venv/bin/python3
TESTER=pytest
LINTER=black

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
env: .venv/bin/activate

.venv/bin/activate: setup.py
ifneq ($(ENV), venv)
	pip install $(ENV)
endif
ifeq ($(ENV), $(filter $(ENV),virtualenv venv))
	test -d .venv || python -m $(ENV) .venv
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --editable .
endif
ifeq ($(ENV), pipenv)
	test -d .venv || pipenv --three
	pipenv update pip
	pipenv install --editable .
endif
ifeq ($(ENV), conda)
	test -d .venv || pipenv --three
	pipenv update pip
	pipenv install --editable .
endif

test: env
	${PYTHON} -m pip install $(TESTER)
	${PYTHON} -m $(TESTER)

lint: env
	${PYTHON} -m pip install $(LINTER)
	${PYTHON} -m $(LINTER)

.PHONY: env test lint