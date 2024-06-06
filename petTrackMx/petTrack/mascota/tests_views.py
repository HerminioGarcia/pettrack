from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Mascota


class MascotaViewsTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba y un grupo 'Administrador'
        self.user = User.objects.create_user(
            username='testuser', password='12345', email='test@example.com')
        self.admin_group = Group.objects.create(name='Administrador')
        self.client = Client()
        self.client.login(username='testuser', password='12345')

        # Crear una mascota de prueba
        self.mascota = Mascota.objects.create(
            user=self.user,
            nombre='Firulais',
            especie='Perro',
            raza='Labrador',
            edad=5,
            numero_telefono='1234567890'
        )

    def test_registrar_mascota_get(self):
        # Prueba acceder a la vista con el método GET
        response = self.client.get(reverse('nueva_convocatoria'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registrar_mascota.html')

    def test_registrar_mascota_post_valid(self):
        # Prueba registrar una mascota con datos válidos
        response = self.client.post(reverse('nueva_convocatoria'), {
            'nombre': 'Rex',
            'especie': 'Perro',
            'raza': 'Golden',
            'edad': 3,
            'numero_telefono': '0987654321'
        })
        # Redirección después del registro exitoso
        self.assertEqual(response.status_code, 302)

    def test_lista_convocatoria_admin(self):
        # Prueba la lista de convocatorias como administrador
        self.user.groups.add(self.admin_group)
        response = self.client.get(reverse('mascotas_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            len(response.context['mascota_list']), Mascota.objects.count())

    def test_lista_convocatoria_user(self):
        # Prueba la lista de convocatorias como usuario regular
        response = self.client.get(reverse('mascotas_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['mascota_list']), Mascota.objects.filter(
            user=self.user).count())

    def test_eliminar_mascota(self):
        # Prueba eliminar una mascota
        response = self.client.post(
            reverse('eliminar_mascota', args=[self.mascota.id]))
        # Redirección después de la eliminación exitosa
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Mascota.objects.filter(id=self.mascota.id).exists())

    def test_editar_mascota_get(self):
        # Prueba acceder a la vista de edición con el método GET
        response = self.client.get(
            reverse('editar_mascota', args=[self.mascota.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editar_mascota.html')

    def test_editar_mascota_post_valid(self):
        # Prueba editar una mascota con datos válidos
        response = self.client.post(reverse('editar_mascota', args=[self.mascota.id]), {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 6,
            'numero_telefono': '1234567890'
        })
        # Redirección después de la edición exitosa
        self.assertEqual(response.status_code, 302)

    def test_registrar_mascota_post_invalid_form(self):
        # Prueba registrar una mascota con un formulario inválido
        response = self.client.post(reverse('nueva_convocatoria'), {})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

    def test_registrar_mascota_post_no_login(self):
        # Prueba registrar una mascota sin estar autenticado
        self.client.logout()
        response = self.client.post(reverse('nueva_convocatoria'), {
            'nombre': 'Luna',
            'especie': 'Gato',
            'raza': 'Siames',
            'edad': 2,
            'numero_telefono': '0123456789'
        })
        # Debería redirigir al login
        self.assertEqual(response.status_code, 302)

    # Pruebas adicionales para ListaConvocatoria
    def test_lista_convocatoria_no_login(self):
        # Prueba acceder a la lista de convocatorias sin estar autenticado
        self.client.logout()
        response = self.client.get(reverse('mascotas_lista'))
        # Debería redirigir al login
        self.assertEqual(response.status_code, 302)

    # Pruebas adicionales para eliminar_mascota
    def test_eliminar_mascota_no_login(self):
        # Prueba eliminar una mascota sin estar autenticado
        self.client.logout()
        response = self.client.post(
            reverse('eliminar_mascota', args=[self.mascota.id]))
        # Debería redirigir al login
        self.assertEqual(response.status_code, 302)

    def test_eliminar_mascota_no_existente(self):
        # Prueba eliminar una mascota que no existe
        response = self.client.post(reverse('eliminar_mascota', args=[999]))
        # Debería retornar error 404
        self.assertEqual(response.status_code, 404)

    # Pruebas adicionales para editar_mascota
    def test_editar_mascota_post_invalid(self):
        # Prueba editar una mascota con datos inválidos
        response = self.client.post(reverse('editar_mascota', args=[self.mascota.id]), {
            'nombre': '',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 6,
            'numero_telefono': '1234567890'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

    def test_editar_mascota_no_login(self):
        # Prueba editar una mascota sin estar autenticado
        self.client.logout()
        response = self.client.post(reverse('editar_mascota', args=[self.mascota.id]), {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 7,
            'numero_telefono': '1234567890'
        })
        self.assertEqual(response.status_code, 302)

    def test_editar_mascota_post_no_changes(self):
        # Prueba editar una mascota sin hacer cambios
        response = self.client.post(reverse('editar_mascota', args=[self.mascota.id]), {
            'nombre': self.mascota.nombre,
            'especie': self.mascota.especie,
            'raza': self.mascota.raza,
            'edad': self.mascota.edad,
            'numero_telefono': self.mascota.numero_telefono
        })
        # Redirección después de la edición sin cambios
        self.assertEqual(response.status_code, 302)

    def test_editar_mascota_post_invalid_phone(self):
        # Prueba editar una mascota con un número de teléfono inválido
        response = self.client.post(reverse('editar_mascota', args=[self.mascota.id]), {
            'nombre': 'Firulais',
            'especie': 'Perro',
            'raza': 'Labrador',
            'edad': 6,
            'numero_telefono': 'invalid'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())

    def test_eliminar_mascota_get_method(self):
        # Prueba eliminar una mascota usando el método GET
        response = self.client.get(
            reverse('eliminar_mascota', args=[self.mascota.id]))
        self.assertEqual(response.status_code, 302)  # Método no permitido

    def test_lista_convocatoria_empty(self):
        # Prueba la lista de convocatorias cuando no hay mascotas
        Mascota.objects.all().delete()
        response = self.client.get(reverse('mascotas_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['mascota_list']), 0)

    def test_registrar_mascota_post_duplicate_phone(self):
        # Prueba registrar una mascota con un número de teléfono duplicado
        response = self.client.post(reverse('nueva_convocatoria'), {
            'nombre': 'Luna',
            'especie': 'Gato',
            'raza': 'Siames',
            'edad': 2,
            'numero_telefono': self.mascota.numero_telefono  # Número duplicado
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
