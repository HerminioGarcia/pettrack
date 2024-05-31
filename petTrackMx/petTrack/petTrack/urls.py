from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from usuarios.routing import websocket_urlpatterns

# Definición de las URL principales del proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Ruta principal que incluye las URLs de la aplicación 'usuarios'
    path('', include('usuarios.urls'), name='bienvenida'),

    # Ruta para la aplicación 'mascota'
    path('Mascotas/', include('mascota.urls')),
]

# Añade rutas para servir archivos estáticos y media en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuración del enrutador de protocolos para manejar WebSocket
#application = ProtocolTypeRouter({
    # (http->django views is added by default)
#    "http": get_asgi_application(),
#    "websocket": AuthMiddlewareStack(
#        URLRouter(
#            websocket_urlpatterns
#        )
#    ),
#})
