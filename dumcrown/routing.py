from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dumcrown.server import consumer

websocket_urlpatterns = [
    # Adicione ".as_asgi()" aqui
    path('ws/game/', consumer.PLayerConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
