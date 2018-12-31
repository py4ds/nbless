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
	pipenv install pip
	pipenv install --editable .
endif

test: env
ifeq ($(TESTER), pytest)
	${PYTHON} -m pip install pytest-mypy
else
	${PYTHON} -m pip install $(TESTER)
endif
	${PYTHON} -m $(TESTER) src tests

lint: env
	${PYTHON} -m pip install $(LINTER)
	${PYTHON} -m $(LINTER) src tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

commit: env
	git commit -am "working on version `python setup.py --version`"
	git push

patch: commit
	bumpversion --current-version `python setup.py --version` patch setup.py

minor: commit
	bumpversion --current-version `python setup.py --version` patch setup.py

dist: clean
	python setup.py sdist bdist_wheel

release: setup.py
	twine upload dist/*

.PHONY: env test lint