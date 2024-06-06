from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from usuarios.models import DatosPersonales, Location, Mascota
from usuarios.forms import FormDatosPersonales, UserForm
import json

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

    def test_bienvenida_view(self):
        response = self.client.get(reverse('bienvenida'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bienvenida.html')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_registrar_view(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword',
        }
        response = self.client.post(reverse('registrar'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_lista_usuarios_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_usuarios.html')
        self.assertContains(response, self.user.username)

    def test_eliminar_usuario_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('eliminar', args=[self.user.id]))
        self.assertRedirects(response, reverse('lista'))

    def test_asignar_grupos_view(self):
        self.client.force_login(self.user)
        data = {'usuario': self.user.id, str(self.grupo.id): 'on'}
        response = self.client.post(reverse('asignar_grupos'), data)
        self.assertRedirects(response, reverse('lista'))
        self.assertTrue(self.user.groups.filter(id=self.grupo.id).exists())

    def test_crear_perfil_view(self):
        self.client.force_login(self.user)
        data = {'nombre': 'Test User', 'edad': 25}
        response = self.client.post(reverse('crear_perfil'), data)
        self.assertRedirects(response, reverse('bienvenida'))
        self.assertTrue(DatosPersonales.objects.filter(user=self.user).exists())

    def test_editar_perfil_view(self):
        self.client.force_login(self.user)
        data = {'nombre': 'Updated User', 'edad': 30}
        response = self.client.post(reverse('editar_perfil', args=[self.datos_personales.id]), data)
        self.assertRedirects(response, reverse('bienvenida'))
        self.datos_personales.refresh_from_db()
        self.assertEqual(self.datos_personales.nombre, 'Updated User')
        self.assertEqual(self.datos_personales.edad, 30)

    def test_homepage_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, self.mascota.nombre)

    def test_arduino_data_view(self):
        data = {
            'latitude': 22.768345,
            'longitude': -102.598677,
            'phone': self.mascota.numero_telefono,
        }
        response = self.client.post(reverse('arduino_data'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'status': 'success', 'message': 'Ubicación actualizada correctamente'})
        self.location.refresh_from_db()
        self.assertEqual(self.location.lat, 22.768345)
        self.assertEqual(self.location.lng, -102.598677)