"""
WSGI config for hotel_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""


import os

if os.environ['ENV'] in ['PRODUCTION']:
    setting = 'hotel_api.settings.production'
else:
    setting = 'hotel_api.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', setting)

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
