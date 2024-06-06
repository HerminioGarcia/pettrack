from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validar_numero_telefono(valor):
    if len(valor) != 10 or not valor.isdigit():
        raise ValidationError(
            "El número de teléfono debe tener exactamente 10 dígitos.")


class Mascota(models.Model):
    user = models.ForeignKey(User, verbose_name="Usuario",
                             related_name='mascota_usuario', on_delete=models.CASCADE)
    nombre = models.CharField("Nombre de la mascota", max_length=300)
    especie = models.CharField(
        "Especie", max_length=300, null=True, blank=True)
    raza = models.CharField('Raza', max_length=300, null=True, blank=True)
    edad = models.IntegerField()
    numero_telefono = models.IntegerField(
        "Número de Teléfono para el arduino",
        unique=True,
    )

    def __str__(self):
        return self.nombre

    def enviar_correo_registro(self):
        """
        Envía un correo electrónico al usuario cuando una mascota es registrada.

        El asunto del correo será 'Mascota [nombre] registrada'.
        El mensaje del correo incluirá el nombre de usuario y el nombre de la mascota.
        """
        asunto = f'Mascota {self.nombre} registrada'
        mensaje = f'Hola {self.user.username},\n\nTu mascota {self.nombre} ha sido registrada con éxito.'
        correo_destino = [self.user.email]
        send_mail(asunto, mensaje, None, correo_destino)

    def enviar_correo_de_eliminacion(self):
        """
        Envía un correo electrónico al usuario cuando una mascota es eliminada.

        El asunto del correo será 'Mascota [nombre] eliminada'.
        El mensaje del correo incluirá el nombre de usuario y el nombre de la mascota.
        """
        asunto = f'Mascota {self.nombre} eliminada'
        mensaje = f'Hola {self.user.username},\n\nTu mascota {self.nombre} ha sido eliminada con éxito.'
        correo_destino = [self.user.email]
        send_mail(asunto, mensaje, None, correo_destino)
