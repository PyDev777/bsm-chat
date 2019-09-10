from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        print('ChatConsumer.connect: START')
        self.accept()
        print('ChatConsumer.connect: FINISH')

    def disconnect(self, close_code):
        print('ChatConsumer.disconnect: ', close_code)
        pass

    def receive(self, text_data):
        print('ChatConsumer.receive: START')

        text_data_json = json.loads(text_data)
        print('ChatConsumer.receive -> text_data_json =', text_data_json)

        message = text_data_json['message']
        print('ChatConsumer.receive -> message =', message)

        self.send(text_data=json.dumps({
            'message': message
        }))
        print('ChatConsumer.receive: FINISH')
