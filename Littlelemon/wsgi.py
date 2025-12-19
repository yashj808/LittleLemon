# This file is the WSGI configuration for the Littlelemon project.
# WSGI (Web Server Gateway Interface) is a specification that describes how a web server communicates with web applications.
# This file is used by web servers to serve the Django application.

"""
WSGI config for Littlelemon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# The DJANGO_SETTINGS_MODULE environment variable tells Django which settings file to use.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Littlelemon.settings')

# The get_wsgi_application() function returns a WSGI application object.
# This object is used by the web server to serve the Django application.
application = get_wsgi_application()