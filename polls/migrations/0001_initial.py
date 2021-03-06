# Generated by Django 3.2.5 on 2021-11-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idComentario', models.CharField(choices=[('1', '1')], max_length=100, verbose_name='Autor del comentario')),
                ('auto', models.CharField(max_length=100, verbose_name='Autor del comentario')),
                ('contenido', models.CharField(max_length=600, verbose_name='Comentario')),
                ('idDestino', models.CharField(max_length=225, verbose_name='Id receta')),
                ('fechaCreacion', models.DateTimeField(verbose_name='Fecha de creación')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idIngrediente', models.CharField(choices=[('1', '1')], max_length=100, verbose_name='Id del ingrendiente')),
                ('nombre', models.CharField(max_length=225, verbose_name='Titulo del ingrediente')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion del ingrediente')),
                ('zonaOrigen', models.CharField(max_length=225, verbose_name='Luegar de origen')),
                ('clasificacion', models.CharField(choices=[('Lacteo', 'Lacteo'), ('Cereales', 'Cereales'), ('Dulces', 'Dulces'), ('Legumbres', 'Legumbres'), ('Fruta', 'Fruta'), ('Verdura', 'Verdura'), ('Carne', 'Carne'), ('Pescados', 'Pescados')], max_length=100, null=True, verbose_name='Clasificacion')),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idReceta', models.CharField(choices=[('1', '1')], max_length=100, verbose_name='Id de la receta')),
                ('titulo', models.CharField(max_length=225, verbose_name='Titulo de la receta')),
                ('descripcion', models.CharField(max_length=500, verbose_name='Descripcion de la receta')),
                ('categoria', models.CharField(choices=[('marina', 'marina'), ('postres', 'postres')], max_length=225, verbose_name='Categoria de la receta')),
                ('ingredientes', models.CharField(max_length=225, verbose_name='Ingredientes de la receta')),
                ('creador', models.EmailField(max_length=225, verbose_name='Creador de la receta')),
                ('opiniones', models.CharField(blank=True, max_length=500, null=True, verbose_name='Opiniones')),
                ('calificacion', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Nombre de la receta')),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(choices=[('1', '1')], max_length=100, verbose_name='Id del Usuario')),
                ('nombre', models.CharField(max_length=225, verbose_name='Nombre del Usuario')),
                ('apellido', models.CharField(max_length=225, verbose_name='Apellido del Usuario')),
                ('apodo', models.CharField(max_length=225, verbose_name='Apodo del Usuario')),
                ('clave', models.CharField(max_length=30, verbose_name='Clave')),
                ('cedula', models.CharField(max_length=30, verbose_name='Cedula del Usuario')),
                ('fechaNacido', models.DateField(verbose_name='Fecha nacimiento')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo del usuario:')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
