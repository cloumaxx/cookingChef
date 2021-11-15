# Generated by Django 3.2.6 on 2021-11-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_receta_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='calificacion',
            field=models.IntegerField(verbose_name='Nombre de la receta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='categoria',
            field=models.CharField(max_length=225, verbose_name='Categoria de la receta'),
        ),
    ]