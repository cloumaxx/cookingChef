# Generated by Django 3.2.5 on 2021-11-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20211121_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_Ingredientes'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_Usuarios'),
        ),
    ]
