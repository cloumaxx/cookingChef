# Generated by Django 3.2.5 on 2021-11-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211121_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='pasosPre',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Como se prepara'),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='idIngrediente',
            field=models.CharField(choices=[('3', '3')], max_length=100, verbose_name='Id del ingrendiente'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.CharField(choices=[('4', '4')], max_length=100, verbose_name='Id del Usuario'),
        ),
    ]
