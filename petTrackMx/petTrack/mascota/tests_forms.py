from django.test import TestCase
from django.contrib.auth.models import User
from .forms import MascotaForm


class MascotaFormTest(TestCase):
    def setUp(self):
        # Crear un usuario para las pruebas
        self.test_user = User.objects.create_user(
            username='testuser', password='12345', email='test@example.com')

    def test_formulario_valido(self):
        form_data = {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 5,
            'numero_telefono': '1234567890',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_formulario_invalido_sin_nombre(self):
        form_data = {
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 5,
            'numero_telefono': '1234567890',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_formulario_invalido_con_numero_telefono_no_numerico(self):
        form_data = {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 5,
            'numero_telefono': 'abcdefghij',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_formulario_invalido_con_campos_vacios(self):
        form_data = {
            'nombre': '',
            'especie': '',
            'raza': '',
            'edad': '',
            'numero_telefono': '',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_formulario_invalido_con_nombre_demasiado_largo(self):
        form_data = {
            'nombre': 'F' * 301,  # 301 caracteres
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 5,
            'numero_telefono': '1234567890',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_formulario_invalido_con_especie_no_proveida(self):
        form_data = {
            'nombre': 'Firulais',
            'raza': 'Labrador',
            'edad': 5,
            'numero_telefono': '1234567890',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertTrue(form.is_valid())  # Especie es opcional

    def test_formulario_invalido_con_raza_no_proveida(self):
        form_data = {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'edad': 5,
            'numero_telefono': '1234567890',
            'user': self.test_user.id
        }
        form = MascotaForm(data=form_data)
        self.assertTrue(form.is_valid())  # Raza es opcional
