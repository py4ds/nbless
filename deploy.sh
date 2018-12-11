#!/usr/bin/env bash

if [ -d "dist" ]; then
    rm dist/*
    echo "Removing previous versions"
fi

python setup.py sdist bdist_wheel

twine upload dist/*