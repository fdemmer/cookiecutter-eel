#!/bin/sh

SCRIPT_PATH="$(cd $(dirname $0);pwd)"

cd ${SCRIPT_PATH}/{{cookiecutter.project_slug}}
python -m eel main.py web --onefile --noconsole
