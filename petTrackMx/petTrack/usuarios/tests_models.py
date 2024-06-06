from sqlite3 import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import DatosPersonales, Location

# modelos de usuario

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

    def test_actualizar_imagen_perfil(self):
        """
        Prueba que se pueda actualizar la imagen de perfil.
        """
        nueva_imagen = 'nueva_imagen.png'
        datos = DatosPersonales.objects.get(user=self.user)
        datos.imag_perfil = nueva_imagen
        datos.save()
        # Verificar que la imagen se haya actualizado correctamente
        self.assertEqual(DatosPersonales.objects.get(pk=datos.pk).imag_perfil, nueva_imagen)

class LocationTests(TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas de Location.
        """
        self.location = Location.objects.create(
            lat=40.7128,
            lng=-74.0060,
            numero_telefono=123456789
        )

    def test_crear_location(self):
        """
        Prueba que la ubicación se crea correctamente.
        """
        location = Location.objects.get(lat=40.7128, lng=-74.0060)
        self.assertEqual(location.numero_telefono, 123456789)

    def test_actualizar_location(self):
        """
        Prueba que la ubicación se actualiza correctamente.
        """
        self.location.numero_telefono = 987654321
        self.location.save()
        location_actualizada = Location.objects.get(lat=40.7128, lng=-74.0060)
        self.assertEqual(location_actualizada.numero_telefono, 987654321)

    def test_borrar_location(self):
        """
        Prueba que la ubicación se borra correctamente.
        """
        self.location.delete()
        with self.assertRaises(Location.DoesNotExist):
            Location.objects.get(lat=40.7128, lng=-74.0060)

    def test_actualizar_coordenadas(self):
        """
        Prueba que se pueda actualizar las coordenadas de ubicación.
        """
        nueva_latitud = -12.345
        nueva_longitud = -67.890
        self.location.lat = nueva_latitud
        self.location.lng = nueva_longitud
        self.location.save()
        # Verificar que las coordenadas se hayan actualizado correctamente
        location_actualizada = Location.objects.get(pk=self.location.pk)
        self.assertEqual(location_actualizada.lat, nueva_latitud)
        self.assertEqual(location_actualizada.lng, nueva_longitud)
    
    # Pruebas adicionales para DatosPersonales

class DatosPersonalesAdditionalTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='testpassword2')
        self.datos = DatosPersonales.objects.create(
            user=self.user,
            nombre='Ana',
            apellidos='Pérez',
            genero='2',
            imag_perfil=None
        )

    def test_validacion_nombre_largo(self):
        """
        Prueba que la validación de longitud máxima del nombre funcione correctamente.
        """
        self.datos.nombre = 'A' * 301  # Nombre más largo que el máximo permitido
        with self.assertRaises(ValidationError):
            self.datos.full_clean()

    def test_validacion_apellidos_largo(self):
        """
        Prueba que la validación de longitud máxima de los apellidos funcione correctamente.
        """
        self.datos.apellidos = 'A' * 301  # Apellidos más largo que el máximo permitido
        with self.assertRaises(ValidationError):
            self.datos.full_clean()

    def test_opcion_genero_invalida(self):
        """
        Prueba que solo se puedan asignar las opciones de género válidas.
        """
        self.datos.genero = '4'  # Opción no válida
        with self.assertRaises(ValidationError):
            self.datos.full_clean()

    def test_cambio_usuario_datos_personales(self):
        """
        Prueba que se pueda cambiar el usuario asociado a los datos personales.
        """
        nuevo_usuario = User.objects.create_user(username='testuser3', password='testpassword3')
        self.datos.user = nuevo_usuario
        self.datos.save()
        self.assertEqual(DatosPersonales.objects.get(pk=self.datos.pk).user, nuevo_usuario)

# Pruebas adicionales para Location

class LocationAdditionalTests(TestCase):
    def setUp(self):
        self.location = Location.objects.create(
            lat=19.4326,
            lng=-99.1332,
            numero_telefono=987654321
        )

    def test_str_location(self):
        """
        Prueba que el método __str__ de Location retorne la cadena correcta.
        """
        self.assertEqual(str(self.location), f"Latitud: {self.location.lat}, Longitud: {self.location.lng} , Telefono_arduino: {self.location.numero_telefono}")

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