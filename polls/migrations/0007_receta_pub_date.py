# Generated by Django 3.2.6 on 2021-11-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_receta_calificacion2'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='pub_date',
            field=models.DateTimeField(default=1, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
