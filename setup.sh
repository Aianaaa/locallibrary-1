#!/bin/sh
python /locallibrary/manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('web_app', 'web-app@never.com', 'supass123')" | ./manage.py shell
python /locallibrary/manage.py init_locallibrary
python /locallibrary/manage.py runserver 0.0.0.0:8000
