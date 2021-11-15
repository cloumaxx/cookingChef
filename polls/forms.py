from django import forms
from polls.models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'idUsuario',
            'nombre',
            'apellido',
            'apodo',
            'clave',
            'cedula',
            'fechaNacido',
            'email'
        ]

        labels = {
            'idUsuario': 'IDUsuario',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'apodo': 'Apodo',
            'clave': 'Clave',
            'cedula': 'Cedula',
            'fechaNacido': 'FechaNacido',
            'email': 'Email',
        }

        widgets = {
            'idUsuario': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingresa el id'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Ingresa tú apellido'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingresa tú apodo'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingresa tú clave'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú cedula'}),
            'fechaNacido': forms.DateTimeInput(attrs={'type': 'date',
                                                      'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú email'}),

        }
