#!/bin/bash -e
set +x

module="src"

uv run mypy $module
uv run ruff check