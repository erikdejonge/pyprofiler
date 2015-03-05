#!/usr/bin/env bash
git commit -am "-"
rm -Rf build
rm -Rf dist
rm -Rf *.egg-info
python setup.py build
python setup.py register
python setup.py sdist
python setup.py sdist upload
git commit -am "-"
git push

