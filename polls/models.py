from django.db import models
import datetime

from django.forms import forms
from django.utils import timezone


class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo de la receta', max_length=225, null=False, blank=False)
    descripcion = models.CharField('Descripcion de la receta', max_length=500, null=False, blank=False)
    categoria = models.CharField('Categoria de la receta', max_length=225, null=False, blank=False)
    ingredientes = models.CharField('Ingredientes de la receta', max_length=225, null=False, blank=False)
    creador = models.EmailField('Creador de la receta', max_length=225, null=False, blank=False)
    opiniones = models.CharField('Opiniones', max_length=100, null=True, blank=True)
    calificacion = models.IntegerField('Nombre de la receta', max_length=225, null=False, blank=False)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
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

    def __str__(self):
        return "{0},{1}".format(self.nombre)


""""
class /Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def publicacionreciente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
*/"""
