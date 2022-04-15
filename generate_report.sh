#!/usr/bin/env bash

echo "-> Generating report"
#cp environment.properties allure-results/
node bdd-report/generate-html-report.js
node bdd-report/generate-multiple-cucumber-html-report.js
echo "-> Open report"
#allure open allure-report/