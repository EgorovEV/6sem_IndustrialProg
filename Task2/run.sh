#!/usr/bin/env bash

#source Task1venv/bin/activate
python manage.py makemigrations TODO_List
python manage.py migrate TODO_List
python manage.py runserver 0.0.0.0:8000
