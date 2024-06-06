from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.forms import UserForm, FormDatosPersonales
from usuarios.models import DatosPersonales
from django.core.exceptions import ValidationError

class TestFormUsuario(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='jorgesolis', password='Jorge123@', email='jasg15_@gmail.com')
        self.data = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123@'
        }
        self.data_invalido = {
            'username': 'jorgeasolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail',
            'repassword': 'Jorge123@'
        }
        self.data_password_invalido = {
            'username': 'jorgesolis',
            'password': 'Jorge123',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123@'
        }
        self.data_password_diferente = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123'
        }
        self.data_password_re_invalido = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123@ '
        }
        self.data_password_re_diferente = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123'
        }
        self.data_password_re_mas_caracteres = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'Jorge123@'*7
        }
        self.data_password_re_min_caracteres = {
            'username': 'jorgesolis',
            'password': 'Jorge123@',
            'email': 'jasg15_@gmail.com',
            'repassword': 'jor'
        }

    def test_usuario_form_valido(self):
        form = UserForm(self.data)
        self.assertTrue(form.is_valid())

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_nombre_invalido_mensaje(self):
        self.data['username'] = 'jorge'
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], ['Nombre de usuario no disponible.'])

    def test_usuario_form_nombre_vacio_mensaje(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['username'], ['Este campo es requerido.'])

    def test_usuario_form_email_invalido(self):
        self.data['email'] = 'jasg15_@gmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_vacio_mensaje(self):
        self.data['email'] = ''
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], ['Este campo es requerido.'])

    def test_usuario_form_email_invalido_mensaje(self):
        self.data['email'] = 'jasg15_@gmail'
        form = UserForm(self.data)
        self.assertEqual(form.errors['email'], ['Este campo debe ser un correo electrónico válido.'])

    def test_usuario_form_password_invalido(self):
        self.data['password'] = 'Jorge123'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_invalido_mensaje(self):
        self.data['password'] = 'Jorge123'
        form = UserForm(self.data)
        self.assertEqual(form.errors['password'], ['Las contraseñas diferentes'])

    def test_usuario_form_password_re_requerido(self):
        self.data['repassword'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_con_espacios(self):
        self.data['repassword'] = 'Jorge123@ '
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_formato_invalido(self):
        self.data['repassword'] = 'jorgeasg'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_diferente_a_password(self):
        self.data['password'] = 'Inventors123@'
        self.data['repassword'] = 'Inventors124@'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_mas_caracteres(self):
        self.data['repassword'] = 'jorgeasg'*7
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_password_re_max_caracteres_mensaje(self):
        self.data['repassword'] = 'jorgeasg'*7
        form = UserForm(self.data)
        self.assertEqual(form.errors['repassword'], ['Las contraseñas diferentes'])

    def test_usuario_form_password_re_min_caracteres(self):
        self.data['repassword'] = 'jor'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

class TestFormDatosPersonales(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'Jorge',
            'apellidos': 'Solís Galván',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_invalido = {
            'nombre': 'Jorge1',
            'apellidos': 'Solís Galván',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_nombre_invalido = {
            'nombre': 'Jorge1',
            'apellidos': 'Solís Galván',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_nombre_vacio = {
            'nombre': '',
            'apellidos': 'Solís Galván',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_nombre_max_caracteres = {
            'nombre': 'Jorges'*10,
            'apellidos': 'Solís Galván',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_apellidos_invalido = {
            'nombre': 'Jorge',
            'apellidos': 'Solís Galván1',
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }
        self.data_apellidos_max_caracteres = {
            'nombre': 'Jorge',
            'apellidos': 'solisg'*10,
            'genero': 'Masculino',
            'imag_perfil': 'C:\\Users\\Lenovo\\Pictures\\3.png'
        }

    def test_datos_personales_form_valido(self):
        form = FormDatosPersonales(self.data)
        self.assertTrue(form.is_valid())

    def test_datos_personales_form_nombre_invalido(self):
        self.data['nombre'] = 'Jorge1'
        form = FormDatosPersonales(self.data)
        self.assertFalse(form.is_valid())

    def test_datos_personales_form_nombre_vacio_mensaje(self):
        self.data['nombre'] = ''
        form = FormDatosPersonales(self.data)
        self.assertEqual(form.errors['nombre'], ['Este campo es requerido.'])

    def test_datos_personales_form_nombre_max_caracteres_mensaje(self):
        self.data['nombre'] = 'Jorges'*10
        form = FormDatosPersonales(self.data)
        self.assertEqual(form.errors['nombre'], ['La longitud máxima del nombre es de 50 caracteres.'])

    def test_datos_personales_form_apellidos_invalido(self):
        self.data['apellidos'] = 'Solís Galván1'
        form = FormDatosPersonales(self.data)
        self.assertFalse(form.is_valid())

    def test_datos_personales_form_apellidos_max_caracteres_mensaje(self):
        self.data['apellidos'] = 'solisg'*10
        form = FormDatosPersonales(self.data)
        self.assertEqual(form.errors['apellidos'], ['La longitud máxima del segundo apellido es de 50 caracteres.'])