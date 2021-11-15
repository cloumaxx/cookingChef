# Generated by Django 3.2.5 on 2021-11-14 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20211114_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='facebook',
            field=models.EmailField(default=1, max_length=100, verbose_name='Facebook del usuario:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='whatsap',
            field=models.IntegerField(default=None, verbose_name='Whatsap usuario:'),
            preserve_default=False,
        ),
    ]