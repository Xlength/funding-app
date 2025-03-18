#!/bin/bash
pip install --upgrade pip && \
pip install django whitenoise gunicorn psycopg2-binary waitress && \
python manage.py migrate && \
python manage.py collectstatic --no-input