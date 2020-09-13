#!/usr/bin/env bash

# fail on first error
set -e

echo "> Starting backend ..."

gunicorn --bin 0.0.0.0:$PORT main:app --timeout 240
