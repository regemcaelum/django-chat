#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    django_asgi_app = get_asgi_application()
    application = ProtocolTypeRouter({
        "http": django_asgi_app,
    })

    ASGI_APPLICATION = 'mysite.asgi.application'
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
