release: python manage.py migrate && python manage.py collectstatic --noinput && python create_superuser.py
web: gunicorn SoftwareApp.wsgi
