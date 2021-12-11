#!/bin/bash -e
set +x

module="src"

autoflake --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports -i -r $module tests
seed-isort-config --application-directories $module &&
isort $module tests
docformatter --in-place -r $module
black $module tests