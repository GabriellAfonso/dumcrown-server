from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dumcrown import consumers

websocket_urlpatterns = [
    # Adicione ".as_asgi()" aqui
    path('ws/game/', consumers.SomeConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})
