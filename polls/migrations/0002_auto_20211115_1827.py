# Generated by Django 3.2.5 on 2021-11-15 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='idIngrediente',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id del ingrendiente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.CharField(choices=[('2', '2')], max_length=100, verbose_name='Id del Usuario'),
        ),
    ]