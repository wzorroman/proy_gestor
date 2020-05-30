"""
WSGI config for proy_gestor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior "apps" directory.
current_path = os.path.dirname(os.path.abspath(__file__))
os.path.realpath(os.path.join(current_path, "apps"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proy_gestor.settings')

application = get_wsgi_application()
