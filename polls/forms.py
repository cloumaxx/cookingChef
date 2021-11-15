from django import forms
from polls.models import Usuario, Ingrediente, Receta


class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = [
            'idIngrediente',
            'nombre',
            'descripcion',
            'zonaOrigen',
            'clasificacion',

        ]
        labels = {
            'idIngrediente': 'IDIngrediente',
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'zonaOrigen': 'ZonaOrigen',
            'clasificacion': 'Clasificacion',

        }
        widgets = {
            'idIngrediente': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'zonaOrigen': forms.TextInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.NumberInput(attrs={'class': 'form-control'})
        }


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'idReceta',
            'titulo',
            'descripcion',
            'categoria',
            'ingredientes',
            'creador',
            'opiniones',
            'calificacion',

        ]
        labels = {
            'idReceta': 'IDReceta',
            'titulo': 'Titulo',
            'descripcion': 'Descripcion',
            'categoria': 'Categoria',
            'ingredientes': 'Ingredientes',
            'creador': 'Creador',
            'opiniones':'Opiniones',
            'calificacion': 'Calificacion',

        }
        widgets = {
            'idReceta': forms.Select(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa el nombre de la receta'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Ingresa la descripcion de la receta'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Ingresa la descripcion de la receta'}),
            'creador': forms.EmailInput(attrs={'class': 'form-control',
                                              'placeholder': 'Ingresa la descripcion de la receta'}),
            'opiniones': forms.TextInput(attrs={'class': 'form-control',
                                              'placeholder': 'Alguna opinion que desees agregar'}),
            'calificacion': forms.Select(attrs={'class': 'form-control', }),

        }


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
            'idUsuario': forms.Select(attrs={'class': 'form-control'}),
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
                                                      'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú email'}),

        }
