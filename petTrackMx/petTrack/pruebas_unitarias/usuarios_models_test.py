from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User  # Import the User class
from usuarios.models import DatosPersonales, Location

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='test_password', email='test@example.com'
        )
        self.datos_personales = DatosPersonales(user=self.user)

    def test_nombre_datos_personales_requerido(self):
        datos_personales = DatosPersonales(nombre='')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_nombre_datos_personales_max_caracteres(self):
        datos_personales = DatosPersonales(nombre='a'*301)
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_nombre_datos_personales_min_caracteres(self):
        datos_personales = DatosPersonales(nombre='n')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_nombre_datos_personales_espacio_al_inicio(self):
        datos_personales = DatosPersonales(nombre=' Nombre')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_apellidos_datos_personales_requerido(self):
        datos_personales = DatosPersonales(apellidos='')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_apellidos_datos_personales_max_caracteres(self):
        datos_personales = DatosPersonales(apellidos='a'*301)
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_apellidos_datos_personales_min_caracteres(self):
        datos_personales = DatosPersonales(apellidos='ap')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_apellidos_datos_personales_espacio_al_inicio(self):
        datos_personales = DatosPersonales(apellidos=' Apellidos')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_genero_datos_personales_requerido(self):
        datos_personales = DatosPersonales(genero='')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_genero_datos_personales_max_caracteres(self):
        datos_personales = DatosPersonales(genero='a'*2)
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_genero_datos_personales_min_caracteres(self):
        datos_personales = DatosPersonales(genero='1')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_genero_datos_personales_espacio_al_inicio(self):
        datos_personales = DatosPersonales(genero=' 1')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_imagen_datos_personales_requerido(self):
        datos_personales = DatosPersonales(imag_perfil='')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_imagen_datos_personales_max_caracteres(self):
        datos_personales = DatosPersonales(imag_perfil='a'*1000001)
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_imagen_datos_personales_min_caracteres(self):
        datos_personales = DatosPersonales(imag_perfil='a')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_imagen_datos_personales_espacio_al_inicio(self):
        datos_personales = DatosPersonales(imag_perfil=' a')
        with self.assertRaises(ValidationError):
            datos_personales.full_clean()

    def test_lat_location_requerido(self):
        location = Location(lat='')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lat_location_max_caracteres(self):
        location = Location(lat='a'*301)
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lat_location_min_caracteres(self):
        location = Location(lat='l')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lat_location_espacio_al_inicio(self):
        location = Location(lat=' Latitud')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lng_location_requerido(self):
        location = Location(lng='')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lng_location_max_caracteres(self):
        location = Location(lng='a'*301)
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lng_location_min_caracteres(self):
        location = Location(lng='l')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_lng_location_espacio_al_inicio(self):
        location = Location(lng=' Longitud')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_numero_telefono_location_requerido(self):
        location = Location(numero_telefono='')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_numero_telefono_location_max_caracteres(self):
        location = Location(numero_telefono='a'*11)
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_numero_telefono_location_min_caracteres(self):
        location = Location(numero_telefono='1')
        with self.assertRaises(ValidationError):
            location.full_clean()

    def test_numero_telefono_location_espacio_al_inicio(self):
        location = Location(numero_telefono=' 1234567890')
        with self.assertRaises(ValidationError):
            location.full_clean()