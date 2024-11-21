"""
ASGI config for yayasan_abc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import threading

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yayasan_abc.settings')

from .grpc_server import grpc_server


application = get_asgi_application()

grpc_thread = threading.Thread(target=grpc_server, daemon=True)
grpc_thread.start()
