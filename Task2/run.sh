#!/usr/bin/env bash

source Task1venv/bin/activate
pip install django~=1.11.0
python manage.py makemigrations TODO_List
python manage.py migrate TODO_List
python manage.py runserver 0.0.0.0:8000
