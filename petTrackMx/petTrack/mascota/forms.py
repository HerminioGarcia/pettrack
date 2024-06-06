from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):
    """
    Formulario para crear y editar mascotas.
    Utiliza el modelo Mascota y excluye el campo 'user' ya que se asigna automáticamente al usuario actual.
    Define los campos y widgets personalizados para la interfaz de usuario.
    """
    class Meta:
        model = Mascota
        # Excluye el campo 'user' para que no se muestre en el formulario
        exclude = ['user']
        fields = '__all__'  # Incluye todos los campos del modelo Mascota en el formulario

        # Define widgets personalizados para cada campo del formulario
        widgets = {
            # Text input con clase 'form-control'
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            # Text input con clase 'form-control'
            'especie': forms.TextInput(attrs={'class': 'form-control'}),
            # Text input con clase 'form-control'
            'raza': forms.TextInput(attrs={'class': 'form-control'}),
            # Number input con clase 'form-control'
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            # Text input con clase 'form-control' y longitud máxima de 10
            'numero_telefono': forms.NumberInput(attrs={'class': 'form-control'}),
        }
