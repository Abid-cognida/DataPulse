#!/bin/bash

# This script runs Celery worker and Flower for development

# Check if the command is provided
if [ -z "$1" ]; then
  echo "Usage: $0 [worker|flower|all]"
  exit 1
fi

# Set environment variables
export PYTHONPATH=$PWD

# Run Celery worker
if [ "$1" = "worker" ] || [ "$1" = "all" ]; then
  echo "Starting Celery worker..."
  poetry run celery -A app.worker worker --loglevel=info
fi

# Run Flower
if [ "$1" = "flower" ] || [ "$1" = "all" ]; then
  echo "Starting Flower..."
  poetry run celery -A app.worker flower --port=5555 --basic_auth=admin:admin
fi
