"""Main entry point """
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

IS_HEROKU = os.environ.get('IS_HEROKU', None)

if IS_HEROKU is None:
    import dev_settings

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangorest.settings')   

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
