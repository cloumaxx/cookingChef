from django import forms
from polls.models import Usuario, Ingrediente, Receta, Comentarios


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields =[
            'idComentario',
            'auto',
            'contenido',
            'idDestino',
            'fechaCreacion',
        ]
        labels = {
            'idComentario':'IDComentario',
            'auto':'Autor',
            'contenido':'Contenido',
            'idDestino':'IDDestino',
            'fechaCreacion':'FechaCreacion',

        }
        widgets = {
            'idComentario': forms.Select(attrs={'class': 'form-control'}),
            'auto': forms.TextInput(attrs={'class': 'form-control','size':'100'}),
            'contenido':forms.Textarea(attrs={'class': 'form-control','size':'100'}),
            'idDestino':forms.TextInput(attrs={'class': 'form-control','size':'100'}),
            'fechaCreacion':forms.DateTimeInput(attrs={'class': 'form-control','type': 'date'}),
        }

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
            'nombre': forms.TextInput(attrs={'class': 'form-control','size':'100'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control','size':'100'}),
            'zonaOrigen': forms.TextInput(attrs={'class': 'form-control','size':'100'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'})
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
                                             'placeholder': 'Ingresa el nombre de la receta','size':'100'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control',
                                                  'placeholder': 'Ingresa la descripcion de la receta','size':'100'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'ingredientes': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Ingresa la descripcion de la receta','size':'100'}),
            'creador': forms.EmailInput(attrs={'class': 'form-control',
                                              'placeholder': 'Ingresa la descripcion de la receta','size':'100'}),
            'opiniones': forms.Textarea(attrs={'class': 'form-control',
                                              'placeholder': 'Alguna opinion que desees agregar','size':'100'}),
            'calificacion': forms.Select(attrs={'class': 'form-control'}),

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
                                             'placeholder': 'Ingresa tú nombre','size':'100'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Ingresa tú apellido','size':'100'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Ingresa tú apodo','size':'100'}),
            'clave': forms.PasswordInput(attrs={'class': 'form-control',
                                                'placeholder': 'Ingresa tú clave','size':'100'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú cedula','size':'100'}),
            'fechaNacido': forms.DateTimeInput(attrs={'type': 'date',
                                                      'class': 'form-control','size':'100'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Ingresa tú email','size':'100'}),

        }
