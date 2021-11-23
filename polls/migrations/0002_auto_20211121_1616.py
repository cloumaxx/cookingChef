# Generated by Django 3.2.5 on 2021-11-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_Recetas'),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='idComentario',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Autor del comentario'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='idIngrediente',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id del ingrendiente'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='idReceta',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id de la receta'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id del Usuario'),
        ),
    ]