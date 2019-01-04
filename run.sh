#!/usr/bin/env bash

if [ ! -d venv ]; then
    echo "Virtualenv does not exist, creating"
    virtualenv venv -p $(which python3)
    source venv/bin/activate
    pip install plexapi
else
    echo "Virtualenv exists, sourcing"
    source venv/bin/activate
fi

echo "Running plex-notifications"
python app.py