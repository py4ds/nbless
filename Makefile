# If ENV is pipenv, run export PIPENV_VENV_IN_PROJECT=1
# Otherwise, .venv will not be in the current project.

README = README.rst
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


.venv/bin/activate: setup.py requirements.txt
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
	pipenv install -r requirements.txt
else
	${PYTHON} -m pip install -r requirements.txt
endif
	touch .venv/bin/activate

test: env
ifeq ($(ENV), pipenv)
	pipenv install pytest-mypy pytest-cov
else
	${PYTHON} -m pip install pytest-mypy pytest-cov
endif
	${PYTHON} -m pytest src tests --verbose --mypy --mypy-ignore-missing-imports --doctest-modules --cov-report term --cov=src/

lint: env
ifeq ($(ENV), pipenv)
	pipenv install $(LINTER)
else
	${PYTHON} -m pip install $(LINTER)
endif
	${PYTHON} -m $(LINTER) src tests

docs/index.html: $(README) $(DOCS) $(TESTS) $(SRC)
	mv docs html
	.venv/bin/sphinx-apidoc -fo html/source src/nbless/ src/nbless/nb*
	.venv/bin/sphinx-apidoc -fo html/source --tocfile test_modules tests
	.venv/bin/sphinx-build -M html html/source .
	mv html docs
	open docs/index.html

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

patch:
	bumpversion patch
	git push origin master --tags

minor:
	bumpversion minor
	git push origin master --tags

major:
	bumpversion major
	git push origin master --tags

dist: clean
	python setup.py sdist bdist_wheel

release: dist
	twine upload dist/*

.PHONY: env test lint clean commit patch minor major dist release