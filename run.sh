#!/usr/bin/env bash

# Plex credentials
echo "Setting Plex Variables"
export PLEX_URL=""
export PLEX_USER=""
export PLEX_PASS=""

# Gmail credentials
echo "Setting GMail Variables"
export GMAIL_USERNAME=""
export GMAIL_PASSWORD=""

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