#!/bin/bash
cd $(dirname $0)
git pull
pipenv install
pipenv run python run.py
