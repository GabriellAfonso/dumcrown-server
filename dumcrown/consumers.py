import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SomeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Chamado quando o WebSocket é aberto.
        await self.accept()

    async def disconnect(self, close_code):
        # Chamado quando o WebSocket é fechado.
        pass

    async def receive(self, text_data):
        # Chamado quando uma mensagem WebSocket é recebida do cliente.
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envie uma mensagem de volta para o cliente.
        await self.send(text_data=json.dumps({
            'message': 'hello client'
        }))
