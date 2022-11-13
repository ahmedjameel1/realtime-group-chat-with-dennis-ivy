import json 

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_room_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.group_room_name,
            self.channel_name,
        )
        self.accept()

    
    def receive(self, text_data):
        text_data = json.loads(text_data)
        message = text_data['message']

        async_to_sync(self.channel_layer.group_send)(
            self.group_room_name,
            {'type': 'chat_messgae', 'message': message}
        )

    def chat_messgae(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
        'type':'chat',
        'message':message
        }))