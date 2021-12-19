#!/bin/bash -e
set +x

module="src"

mypy $module
black $module --check
black tests --check
flake8