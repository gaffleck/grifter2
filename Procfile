release: python manage.py migrate
web: gunicorn djangorest.wsgi
worker: python api/worker.py