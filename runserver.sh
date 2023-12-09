#/bin/bash

python manage.py migrate
python manage.py runserver localhost:8000
