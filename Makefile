# If ENV is pipenv, run export PIPENV_VENV_IN_PROJECT=1
# Otherwise, .venv will not be in the current project.

ENV = venv
PYTHON = .venv/bin/python3
LINTER = black
DOCS = $(wildcard docs/source/*.rst docs/source/*.md docs/source/*.ipynb)
TESTS = $(wildcard tests/*.py)
SRC = $(wildcard src/*/*.py)


init: .git/
env: .venv/bin/activate
docs: docs/index.html
patch-release: patch release


.venv/bin/activate: setup.py
ifneq ($(ENV), $(filter $(ENV),conda venv))
	pip install $(ENV)
endif
ifeq ($(ENV), $(filter $(ENV),virtualenv venv))
	test -d .venv || python -m $(ENV) .venv
endif
ifeq ($(ENV), conda)
	test -d .venv || conda create -yp .venv python=3
endif
ifeq ($(ENV), pipenv)
	test -d .venv || pipenv --three
	pipenv install pip
	pipenv install --editable .
else
	${PYTHON} -m pip install --editable .
endif
	touch .venv/bin/activate

test: env
ifeq ($(ENV), pipenv)
	pipenv install pytest-mypy
else
	${PYTHON} -m pip install pytest-mypy
endif
	${PYTHON} -m pytest src tests

lint: env
ifeq ($(ENV), pipenv)
	pipenv install $(LINTER)
else
	${PYTHON} -m pip install $(LINTER)
endif
	${PYTHON} -m $(LINTER) src tests

docs/index.html: $(DOCS) $(TESTS) $(SRC)
	mv docs html
	sphinx-apidoc -fo html/source src/nbless
	sphinx-apidoc -fo html/source --tocfile tests tests
	sphinx-build -M html html/source .
	mv html docs
	open docs/index.html

git:
	git add --all
	[ -z "`git status --porcelain`" ] || git commit
	git push

clean:
	rm -rf docs/_modules
	rm -rf docs/searchindex.js
	rm -rf docs/_sources
	rm -rf docs/doctrees
	rm -rf doctrees
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

patch: git
	bumpversion --current-version `python setup.py --version` patch setup.py
	git commit --all --message "Bump version to `python setup.py --version`"
	git push

minor: git
	bumpversion --current-version `python setup.py --version` minor setup.py
	git commit --all --message "Bump version to `python setup.py --version`"
	git push

major: git
	bumpversion --current-version `python setup.py --version` major setup.py
	git commit --all --message "Bump version to `python setup.py --version`"
	git push

dist: clean
	python setup.py sdist bdist_wheel

release: dist
	twine upload dist/*

.PHONY: env test lint clean commit patch minor major dist release