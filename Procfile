release: python manage.py migrate
web: gunicorn djangorest.wsgi
worker: python manage.py rqworker default