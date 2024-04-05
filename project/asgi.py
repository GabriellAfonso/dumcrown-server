import os
from django.urls import re_path
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import dumcrown.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
print('to aqui asgi')
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            dumcrown.routing.websocket_urlpatterns
        ),
    ),
})
