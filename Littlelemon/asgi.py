# This file is the ASGI configuration for the Littlelemon project.
# ASGI (Asynchronous Server Gateway Interface) is a specification that describes how a web server communicates with asynchronous web applications.
# This file is used by web servers to serve the Django application in an asynchronous manner.
# Asynchronous applications can handle many connections at the same time, which can improve performance.

"""
ASGI config for Littlelemon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# The DJANGO_SETTINGS_MODULE environment variable tells Django which settings file to use.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Littlelemon.settings')

# The get_asgi_application() function returns an ASGI application object.
# This object is used by the web server to serve the Django application.
application = get_asgi_application()