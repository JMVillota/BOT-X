"""
WSGI config for BotIQ project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BotIQ.settings')

application = get_wsgi_application()

if __name__ == "__main__":
    # Ejecuta la aplicación Django
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
