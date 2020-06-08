#!/bin/sh

python manage.py flush --no-input
python manage.py migrate

gunicorn -b "0.0.0.0:8080" website.wsgi