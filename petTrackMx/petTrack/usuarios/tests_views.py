from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from .models import DatosPersonales, Location
from mascota.models import Mascota
from .views import CustomPasswordResetView

class CustomPasswordResetViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')

    def test_email_context(self):
        """
        Prueba que el contexto del correo electrónico se actualice correctamente.
        """
        request = self.factory.post('/password_reset/')
        request.user = self.user
        context = {
            'user': self.user,
            'token': default_token_generator.make_token(self.user),
        }
        view = CustomPasswordResetView()
        view.request = request

        protocol = request.scheme
        domain = request.META.get('HTTP_HOST', 'example.com')
        uid = urlsafe_base64_encode(force_bytes(context['user'].pk))


        context.update({
            'protocol': protocol,
            'domain': domain,
            'uid': uid,
            'token': context['token'],
            'timeout': 24,  # Ajusta esto según tu configuración
        })

        self.assertEqual(context['protocol'], request.scheme)
        self.assertEqual(context['domain'], request.META.get('HTTP_HOST', 'example.com'))
        self.assertEqual(context['uid'], uid)
        self.assertEqual(context['token'], context['token'])
        self.assertEqual(context['timeout'], 24)

class LoginViewTests(TestCase):
    def test_login_view(self):
        """
        Prueba que la vista de inicio de sesión renderice el template correcto.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.grupo = Group.objects.create(name='Test Group')
        self.datos_personales = DatosPersonales.objects.create(
            user=self.user, nombre='Test User', edad=25)
        self.mascota = Mascota.objects.create(
            user=self.user, nombre='Test Mascota', numero_telefono='1234567890')
        self.location = Location.objects.create(
            numero_telefono=self.mascota.numero_telefono, lat=22.768345, lng=-102.598677)
