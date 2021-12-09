#!/bin/bash -e
set +x

module="src"

mypy $module
black $module --check
black tests --check
isort --check-only $module tests
flake8