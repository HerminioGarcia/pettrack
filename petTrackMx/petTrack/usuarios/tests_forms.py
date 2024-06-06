from django.test import TestCase
from django.contrib.auth.models import User
from .forms import UserForm, FormDatosPersonales
from .models import DatosPersonales
from django.core.files.uploadedfile import SimpleUploadedFile


class UserFormTests(TestCase):
    def test_save_user(self):
        """
        Prueba que el formulario guarde un usuario correctamente.
        """
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
            'repassword': 'testpassword',
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, User)

    def test_clean_password(self):
        """
        Prueba que el método clean_password levante una excepción si las contraseñas no coinciden.
        """
        form_data = {
            'password': 'password1',
            'repassword': 'password2',
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_clean_username(self):
        """
        Prueba que el método clean_username levante una excepción si el nombre de usuario ya existe.
        """
        User.objects.create(username='existinguser')
        form_data = {
            'username': 'existinguser',
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class FormDatosPersonalesTests(TestCase):
    def test_save_datos_personales(self):
        """
        Prueba que el formulario guarde datos personales correctamente.
        """
        user = User.objects.create(username='testuser', password='testpassword')
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            'genero': '1',
            'imag_perfil': None,
        }
        form = FormDatosPersonales(data=form_data)
        self.assertTrue(form.is_valid())
        datos_personales = form.save(commit=False)
        datos_personales.user = user
        datos_personales.save()
        self.assertEqual(datos_personales.nombre, 'John')

    def test_form_widgets(self):
        """
        Prueba que los widgets se asignen correctamente en el formulario.
        """
        form = FormDatosPersonales()
        self.assertIn('class="form-control"', str(form['nombre']))
        self.assertIn('class="form-control"', str(form['apellidos']))
        self.assertIn('class="form-control"', str(form['genero']))
        self.assertIn('class="form-control"', str(form['imag_perfil']))

    def test_clean_genero(self):
        """
        Prueba que el método clean_genero levante una excepción si se proporciona un valor no válido.
        """
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            'genero': '4',  # Valor no válido
        }
        form = FormDatosPersonales(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('genero', form.errors)

    def test_valid_email(self):
        """
        Prueba que el correo electrónico sea válido.
        """
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'invalid_email',  # Correo electrónico inválido
            'repassword': 'testpassword',
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_valid_imag_perfil(self):
        """
        Prueba que la imagen de perfil sea válida.
        """
        # Supongamos que 'valid_image.png' es una imagen válida
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            'genero': '1',
            'imag_perfil': 'valid_image.png',
        }
        form = FormDatosPersonales(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_imag_perfil(self):
        """
        Prueba que la imagen de perfil sea inválida.
        """
        # Supongamos que 'invalid_image.txt' no es una imagen válida
        # Crea un archivo de texto vacío para simular una imagen inválida
        file_data = b''
        image_file = SimpleUploadedFile('invalid_image.txt', file_data)
    
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            'genero': '1',
        }
        # Añade el archivo de imagen al formulario
        form = FormDatosPersonales(data=form_data, files={'imag_perfil': image_file})
    
        # Verifica que el formulario sea inválido
        self.assertFalse(form.is_valid())
        # Verifica que 'imag_perfil' esté en los errores del formulario
        self.assertIn('imag_perfil', form.errors)

    def test_max_length_nombre_apellidos(self):
        """
        Prueba que el nombre y los apellidos no superen la longitud máxima permitida.
        """
        form_data = {
            'nombre': 'J' * 301,  # Longitud mayor a la permitida
            'apellidos': 'D' * 301,  # Longitud mayor a la permitida
            'genero': '1',
            'imag_perfil': None,
        }
        form = FormDatosPersonales(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)
        self.assertIn('apellidos', form.errors)

    def test_unique_username(self):
        """
        Prueba que el nombre de usuario sea único.
        """
        User.objects.create(username='existinguser')
        form_data = {
            'username': 'existinguser',  # Nombre de usuario existente
        }
        form = UserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class DatosPersonalesTests(TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas de DatosPersonales.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.datos = DatosPersonales.objects.create(
            user=self.user,
            nombre='John',
            apellidos='Doe',
            genero='1',
            imag_perfil=None
        )

    def test_crear_datos_personales(self):
        """
        Prueba que los datos personales se crean correctamente.
        """
        datos = DatosPersonales.objects.get(user=self.user)
        self.assertEqual(datos.nombre, 'John')
        self.assertEqual(datos.apellidos, 'Doe')
        self.assertEqual(datos.genero, '1')

    def test_actualizar_datos_personales(self):
        """
        Prueba que los datos personales se actualizan correctamente.
        """
        self.datos.nombre = 'Jane'
        self.datos.save()
        datos_actualizados = DatosPersonales.objects.get(user=self.user)
        self.assertEqual(datos_actualizados.nombre, 'Jane')

    def test_borrar_datos_personales(self):
        """
        Prueba que los datos personales se borran correctamente.
        """
        self.datos.delete()
        with self.assertRaises(DatosPersonales.DoesNotExist):
            DatosPersonales.objects.get(user=self.user)
    
    # Pruebas adicionales para UserForm

class UserFormAdditionalTests(TestCase):
    
    def test_genero_default(self):
        """
        Prueba que el género tenga un valor por defecto si no se proporciona uno.
        """
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            # Campo género no proporcionado
        }
        form = FormDatosPersonales(data=form_data)
        self.assertTrue(form.is_valid())
        datos_personales = form.save(commit=False)
        self.assertEqual(datos_personales.genero, '1')  # Verificar valor por defecto

    def test_imag_perfil_file_size(self):
        """
        Prueba que la imagen de perfil no exceda el tamaño máximo permitido.
        """
        # Supongamos que 'large_image.jpg' es una imagen demasiado grande
        large_image_data = b'\x00\x01' * (2 * 1024 * 1024)  # 2MB
        large_image_file = SimpleUploadedFile('large_image.jpg', large_image_data, content_type='image/jpeg')
    
        form_data = {
            'nombre': 'John',
            'apellidos': 'Doe',
            'genero': '1',
        }
        # Añade el archivo de imagen grande al formulario
        form = FormDatosPersonales(data=form_data, files={'imag_perfil': large_image_file})
    
        # Verifica que el formulario sea inválido y que el tamaño del archivo sea el problema
        self.assertFalse(form.is_valid())
        self.assertIn('imag_perfil', form.errors)

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

    def test_usuario_form_nombre_vacio(self):
        self.data['username'] = ''
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

    def test_usuario_form_email_invalido(self):
        self.data['email'] = 'jasg15_@gmail'
        form = UserForm(self.data)
        self.assertFalse(form.is_valid())

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

    def test_datos_personales_form_nombre_invalido(self):
        self.data['nombre'] = 'Jorge1'
        form = FormDatosPersonales(self.data)
        self.assertFalse(form.is_valid())

    def test_datos_personales_form_apellidos_invalido(self):
        self.data['apellidos'] = 'Solís Galván1'
        form = FormDatosPersonales(self.data)
        self.assertFalse(form.is_valid())
        