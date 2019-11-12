"""
ASGI entrypoint. Configures Django and then runs the application
defined in the ASGI_APPLICATION setting.

RUN:
daphne -p 8001 myproject.asgi:application
daphne -b 0.0.0.0 -p 8001 myproject.asgi:application
"""
import os
import django
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bsmdb.settings')
django.setup()
application = get_default_application()
