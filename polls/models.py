from django.db import models
import datetime

from django.forms import forms
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Comentarios(models.Model):
    idComentario = models.AutoField(primary_key=True)
    auto =models.CharField('Autor del comentario',max_length=100,null=False,blank=False)
    contenido= models.CharField('Comentario',max_length=600,null=False,blank=False)
    idDestino = models.CharField('Id receta', max_length=225, null=False, blank=False)
    fechaCreacion = models.DateTimeField('Fecha de creación', null=False, blank=False)


class Receta(models.Model):
    pub_date = models.DateTimeField('date published')

    idReceta = models.AutoField(primary_key=True)
#    id =models.models.CharField('id de la receta', max_length=225, null=False, blank=False)
    titulo = models.CharField('Titulo de la receta', max_length=225, null=False, blank=False)
    descripcion = models.CharField('Descripcion de la receta', max_length=500, null=False, blank=False)
    categoria = models.CharField('Categoria de la receta', max_length=225, null=False, blank=False)
    ingredientes = models.CharField('Ingredientes de la receta', max_length=225, null=False, blank=False)
    creador = models.EmailField('Creador de la receta', max_length=225, null=False, blank=False)
    opiniones = models.CharField('Opiniones', max_length=100, null=True, blank=True)
    calificacion = models.IntegerField('Nombre de la receta', max_length=1, null=False, blank=False)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

   # def __str__(self):
    #    return self.titulo


class Ingrediente(models.Model):
    idIngrediente = models.AutoField(primary_key=True)
    nombre = models.CharField('Titulo del ingrediente', max_length=225, null=False, blank=False)
    descripcion = models.CharField('Descripcion del ingrediente', max_length=500, null=False, blank=False)
    zonaOrigen = models.CharField('Luegar de origen', max_length=225, null=False, blank=False)
    clasificacion = models.CharField('Clasificacion', max_length=100, null=True, blank=True)


    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    #def __str__(self):
    #}    return self.nombre


class Usuario(models.Model):
    pub_date = models.DateTimeField('date published')

    idUsuario = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre del Usuario', max_length=225, null=False, blank=False)
    apellido = models.CharField('Apellido del Usuario', max_length=225, null=False, blank=False)
    apodo = models.CharField('Apodo del Usuario', max_length=225, null=False, blank=False)
    clave = models.CharField('Clave', max_length=30, null=False, blank=False)
    cedula = models.CharField('Cedula del Usuario', max_length=30, null=False, blank=False)
    fechaNacido = models.DateField('Fecha nacimiento', auto_now=False, null=False, blank=False)
    email = models.EmailField('Correo del usuario:', null=False, blank=False)
    Facebook = models.URLField('Facebook:', null=True, blank=True)
    whatsapp = models.URLField('Whatsapp:', null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

   # def __str__(self):
        #return "{0},{1}".format(self.nombre)


