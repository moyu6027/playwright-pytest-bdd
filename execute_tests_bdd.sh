#!/usr/bin/env bash
source /opt/venv/bin/activate
#echo "-> Installing dependencies"
#python3 -m pip install --upgrade pip
#python3 -m playwright install
#pip3 install -r requirements.txt --quiet
#
#echo "-> Removing old results"
#rm -r .report.json || echo "No results"
#export BASE_URL=http://automationpractice.com
export BASE_URL=https://github.com
echo "-> Start tests"
pytest --base-url $BASE_URL tests/step_definition/test_visit_github_project.py

echo "-> Test finished"