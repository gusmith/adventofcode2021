#!/bin/bash -e
set +x

module="src"

mypy $module
ruff check