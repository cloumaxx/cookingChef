# Generated by Django 3.2.5 on 2021-11-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20211121_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_Recetas'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes_Recetas'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='categoria',
            field=models.CharField(choices=[('marina', 'marina'), ('postres', 'postres'), ('tipico', 'tipico')], max_length=225, verbose_name='Categoria de la receta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='idReceta',
            field=models.CharField(choices=[('4', '4')], max_length=100, verbose_name='Id de la receta'),
        ),
    ]
