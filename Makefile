ENV_NAME=.venv
ENV_TOOL=virtualenv
ENV_ACTIVATE=. $(ENV_NAME)/bin/activate
PYTHON=${ENV_NAME}/bin/python3
TESTER=pytest
LINTER=black

# Requirements are in setup.py, so whenever setup.py is changed, re-run installation of dependencies.
env: $(ENV_NAME)/bin/activate
$(ENV_NAME)/bin/activate: setup.py
ifneq ($(ENV_TOOL), venv)
	pip install $(ENV_TOOL)
endif
ifeq ($(ENV_TYPE), $(filter $(ENV_TYPE),virtualenv venv))
	test -d $(ENV_NAME) || python -m $(ENV_TOOL) $(ENV_NAME)
endif
ifeq ($(ENV_TYPE), pipenv)
	export PIPENV_VENV_IN_PROJECT=1
	test -d $(ENV_NAME) || python -m $(ENV_TOOL) $(ENV_NAME)
endif
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -e .

test: env
	pip install $(TESTER)
	${PYTHON} -m $(TESTER)

lint: env
	pip install $(LINTER)
	${PYTHON} -m $(LINTER)

.PHONY: env test lint run