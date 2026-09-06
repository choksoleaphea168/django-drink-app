#!/bin/bash
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt --break-system-packages

echo "Collecting static files..."
mkdir -p staticfiles_build/static
python3 manage.py collectstatic --noinput --clear
