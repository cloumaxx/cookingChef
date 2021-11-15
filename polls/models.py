from django.db import models
from django.db import connection

import datetime

from django.forms import forms
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Comentarios(models.Model):
    idComentario = models.AutoField(primary_key=True)
    auto = models.CharField('Autor del comentario', max_length=100, null=False, blank=False)
    contenido = models.CharField('Comentario', max_length=600, null=False, blank=False)
    idDestino = models.CharField('Id receta', max_length=225, null=False, blank=False)
    fechaCreacion = models.DateTimeField('Fecha de creación', null=False, blank=False)


def calcularCodigoReceta():
    with connection.cursor() as cursor:
        cursor.execute('SELECT  MAX("idReceta") \n FROM public.polls_receta;')
        row = cursor.fetchone()
    aux = str(row)
    num = int(aux[2])
    final = num + 1

    return final



def calcularCodigoIngre():
    with connection.cursor() as cursor:
        cursor.execute('SELECT  MAX("idIngrediente") \n FROM public.polls_ingrediente;')
        row = cursor.fetchone()
    aux = str(row)
    num = int(aux[2])
    final = num + 1

    return final


class Ingrediente(models.Model):
    aux = str(calcularCodigoIngre())
    CodigoReceta = [(aux, aux)]
    tipoComida = [('Lacteo', 'Lacteo'),
                  ('Cereales', 'Cereales'),
                  ('Dulces', 'Dulces'),
                  ('Legumbres', 'Legumbres'),
                  ('Fruta', 'Fruta'),
                  ('Verdura', 'Verdura'),
                  ('Carne', 'Carne'),
                  ('Pescados', 'Pescados'),
                  ]
    idIngrediente = models.CharField('Id del ingrendiente', max_length=100, null=False, choices=CodigoReceta)
    nombre = models.CharField('Titulo del ingrediente', max_length=225, null=False, blank=False)
    descripcion = models.CharField('Descripcion del ingrediente', max_length=500, null=False, blank=False)
    zonaOrigen = models.CharField('Luegar de origen', max_length=225, null=False, blank=False)
    clasificacion = models.CharField('Clasificacion', max_length=100, null=True, choices=tipoComida)

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return "{}".format(self.nombre)


def calcularCodigoUsua():
    with connection.cursor() as cursor:
        cursor.execute('SELECT  MAX("idUsuario") \n FROM public.polls_usuario;')
        row = cursor.fetchone()
    aux = str(row)
    num = int(aux[2])
    final = num + 1

    return final


class Receta(models.Model):
    aux = '1'  # str(calcularCodigoReceta())
    CodigoReceta = [(aux, aux)]
    calificaciones = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    categorias = [
        ('marina', 'marina'),
        ('postres', 'postres')
    ]
    idReceta = models.CharField('Id de la receta', max_length=100, null=False, choices=CodigoReceta)
    titulo = models.CharField('Titulo de la receta', max_length=225, null=False, blank=False)
    descripcion = models.CharField('Descripcion de la receta', max_length=500, null=False, blank=False)
    categoria = models.CharField('Categoria de la receta', max_length=225, choices=categorias)
    ingredientes = models.CharField('Ingredientes de la receta', max_length=225, null=False, blank=False)
    creador = models.EmailField('Creador de la receta', max_length=225, null=False, blank=False)
    opiniones = models.CharField('Opiniones', max_length=500, null=True, blank=True)
    calificacion = models.IntegerField('Nombre de la receta', choices=calificaciones)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return "{}".format(self.titulo)

# aux
class Usuario(models.Model):
    aux = str(calcularCodigoUsua())
    CodigoUsuario = [(aux, aux)]

    idUsuario = models.CharField('Id del Usuario', max_length=100, null=False, choices=CodigoUsuario)
    nombre = models.CharField('Nombre del Usuario', max_length=225, null=False, blank=False)
    apellido = models.CharField('Apellido del Usuario', max_length=225, null=False, blank=False)
    apodo = models.CharField('Apodo del Usuario', max_length=225, null=False, blank=False)
    clave = models.CharField('Clave', max_length=30, null=False, blank=False)
    cedula = models.CharField('Cedula del Usuario', max_length=30, null=False, blank=False)
    fechaNacido = models.DateField('Fecha nacimiento', auto_now=False, null=False, blank=False)
    email = models.EmailField('Correo del usuario:', null=False, blank=False)

    # facebook = models.EmailField('Facebook del usuario:',max_length=100)
    # whatsapp = models.IntegerField('Whatsap usuario:')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return "{}".format(self.nombre)
