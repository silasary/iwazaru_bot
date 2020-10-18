#!/bin/bash
cd "$(dirname "$0")" || exit 1
git pull
pipenv install
pipenv run python run.py
