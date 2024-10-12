#!/bin/env bash

echo "Start ${ENVIRONMENT} server"
if [[ "${ENVIRONMENT}" = "PRODUCTION" ]]; then
    echo "Starting FastAPI app in production mode..."
    # No auto-reload, production settings
    poetry run uvicorn main:FAST_API_APP --host 0.0.0.0 --port 8000 --workers 4
elif [[ "${ENVIRONMENT}" = "DEVELOP" ]]; then
    echo "Starting FastAPI app in development mode..."
    # Using auto-reload and debug mode for development
    poetry run uvicorn main:FAST_API_APP --reload --host 0.0.0.0 --port 8000
fi
