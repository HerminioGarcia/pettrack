from channels.generic.websocket import WebsocketConsumer
# import json


class ArduinoConsumer(WebsocketConsumer):
    pass
    # def connect(self):
    # Acepta la conexión WebSocket
    # self.accept()

    # def disconnect(self, close_code):
    # Maneja la desconexión WebSocket
    # pass

    # def receive(self, text_data):
    # print("entra aqui")
    # Este método se llama cuando se recibe un mensaje del WebSocket
    # text_data_json = json.loads(text_data)
    # message = text_data_json['message']

    # Imprime el mensaje para depuración
    # print("Mensaje recibido:", message)

    # Envía el mensaje a través del WebSocket a todos los clientes conectados
    # self.send(text_data=json.dumps({
    #     'message': message
    # }))
