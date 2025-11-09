"""
WSGI config for location_visualizer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Updated to point to the new settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'location_visualizer.settings')

application = get_wsgi_application()