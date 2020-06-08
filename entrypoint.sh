#!/bin/sh

export SQL_DATABASE=aegee
export SQL_USER=aegee
export SQL_PASSWORD=erasmusmundus
export SQL_HOST=127.0.0.1
export SQL_PORT=5432
export ADMIN_USER=admin
export ADMIN_PASSWORD=erasmusmundus

python manage.py flush --no-input
python manage.py migrate

gunicorn -b "0.0.0.0:8080" website.wsgi