#!/bin/bash -e
set +x

module="src"

seed-isort-config --application-directories $module
isort $module
black $module