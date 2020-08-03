#!/bin/bash

export NETNIR_USER=bogus
export NETNIR_PASS=bogus
python3 -m venv env
source ./env/bin/activate
./setup.py install
pip install sphinx recommonmark sphinx_rtd_theme recommonmark
cd docs/_mkdocs
sphinx-apidoc -f -o netnir ../../netnir
make clean
make dirhtml
rsync -avz --exclude sphinx-env ./_build/dirhtml/ ..
cd -
rm -rf env
./clean.sh