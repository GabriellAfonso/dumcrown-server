import json
import jwt
from .codes import code_handlers
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings


class PLayerConsumer(AsyncWebsocketConsumer):
    async def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id

    async def connect(self):
        # Chamado quando o WebSocket é aberto.

        # Exemplo de como obter o token dos parâmetros de consulta
        token = self.scope['query_string'].decode("utf-8").split('=')[1]

        try:
            # Validar o token JWT
            decoded_token = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])

            if self.user_has_permission(decoded_token['user_id']):
                await self.accept()
                self.user_id = decoded_token
                await self.send(text_data=json.dumps({
                    'code': 'connected',
                    'data': '',
                }))
            else:
                self.close()
        except jwt.ExpiredSignatureError:
            # Token expirado
            self.close()
        except jwt.InvalidTokenError:
            # Token inválido
            self.close()

        # print("Scope:", self.scope)

    async def user_has_permission(self, user_id):
        # Verifique se o usuário tem permissão para se conectar
        # Você pode implementar sua lógica de verificação de permissão aqui
        return True  # Substitua isso com sua lógica real

    async def disconnect(self, close_code):
        # Chamado quando o WebSocket é fechado.
        pass

    async def receive(self, text_data):
        # Chamado quando uma mensagem WebSocket é recebida do cliente.

        message = json.loads(text_data)

        for code, handler_name in code_handlers.items():
            if code in message["code"]:
                handler = getattr(self, handler_name)
                await handler(message['data'])

    async def send_pong(self, data):
        await self.send(text_data=json.dumps({
            'code': 'pong',
            'data': '',
        }))
