#!/bin/bash

pushd ~
mkdir tmp-fedora-update
pushd tmp-fedora-update
wget -d https://raw.githubusercontent.com/cccslab/fedora-utils/master/updater/updater.py
wget -d https://raw.githubusercontent.com/cccslab/fedora-utils/master/updater/client_secrets.json
python updater.py
popd
rm -rf tmp-fedora-update
popd

