from django.test import TestCase
from django.contrib.auth.models import User
from .models import Mascota
from django.core import mail
from django.db import IntegrityError


class MascotaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un usuario para la prueba
        test_user = User.objects.create_user(
            username='testuser', password='12345', email='test@example.com')
        test_user.save()

        # Crear una instancia de Mascota para la prueba
        Mascota.objects.create(
            user=test_user,
            nombre='Firulais',
            especie='Perro',
            raza='Labrador',
            edad=5,
            numero_telefono='1234567890'
        )

    def test_edad_positiva(self):
        mascota = Mascota.objects.get(id=1)
        self.assertGreaterEqual(
            mascota.edad, 0, 'La edad de la mascota debe ser un número positivo.')

    def test_numero_telefono_valido(self):
        mascota = Mascota.objects.get(id=1)
        numero_telefono = str(mascota.numero_telefono)
        self.assertEqual(len(numero_telefono), 10,
                         'El número de teléfono debe tener 10 dígitos.')

    def test_str_representation(self):
        mascota = Mascota.objects.get(id=1)
        self.assertEqual(str(mascota), 'Firulais',
                         'La representación en cadena del modelo Mascota debe ser el nombre de la mascota.')

    def test_enviar_correo_registro(self):
        mascota = Mascota.objects.get(id=1)
        mascota.enviar_correo_registro()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         f'Mascota {mascota.nombre} registrada')

    def test_enviar_correo_de_eliminacion(self):
        mascota = Mascota.objects.get(id=1)
        mascota.enviar_correo_de_eliminacion()
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         f'Mascota {mascota.nombre} eliminada')

    def test_numero_telefono_unico(self):
        try:
            Mascota.objects.create(
                user=User.objects.get(username='testuser'),
                nombre='Rex',
                especie='Perro',
                raza='Golden Retriever',
                edad=4,
                numero_telefono='1234567890'  # Número ya utilizado en setUpTestData
            )
            self.fail('IntegrityError no fue lanzado')
        except IntegrityError:
            pass

    def test_especie_raza_no_vacios(self):
        mascota = Mascota.objects.get(id=1)
        self.assertTrue(
            mascota.especie, 'El campo especie no debe estar vacío si se proporciona.')
        self.assertTrue(
            mascota.raza, 'El campo raza no debe estar vacío si se proporciona.')

    def test_longitud_maxima_campos(self):
        mascota = Mascota.objects.get(id=1)
        self.assertLessEqual(len(
            mascota.nombre), 300, 'El nombre de la mascota debe tener como máximo 300 caracteres.')
        self.assertLessEqual(len(mascota.especie), 300,
                             'La especie de la mascota debe tener como máximo 300 caracteres.')
        self.assertLessEqual(len(
            mascota.raza), 300, 'La raza de la mascota debe tener como máximo 300 caracteres.')

    def test_cascading_delete(self):
        user = User.objects.get(username='testuser')
        user.delete()
        self.assertFalse(Mascota.objects.filter(user=user).exists(
        ), 'Las mascotas asociadas al usuario deben eliminarse en cascada.')
