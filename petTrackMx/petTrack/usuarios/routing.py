from django.urls import path
from .consumers import ArduinoConsumer
from . import views

websocket_urlpatterns = [
    path('ws/arduino/', ArduinoConsumer.as_asgi()),
    #path('arduino_data/', views.arduino_data, name='arduino_data'),
]

