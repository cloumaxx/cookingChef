# Generated by Django 3.2.5 on 2021-11-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211115_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='idComentario',
            field=models.CharField(choices=[('1', '1')], max_length=100, verbose_name='Id de la receta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='idReceta',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id de la receta'),
        ),
    ]