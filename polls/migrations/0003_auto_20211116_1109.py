# Generated by Django 3.2.6 on 2021-11-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211116_1027'),
    ]

    operations = [
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