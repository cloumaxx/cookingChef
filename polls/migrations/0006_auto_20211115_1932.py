# Generated by Django 3.2.5 on 2021-11-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20211115_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarios',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='idComentario',
            field=models.CharField(max_length=100, verbose_name='Autor del comentario'),
        ),
    ]