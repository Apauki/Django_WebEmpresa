# Generated by Django 4.1.6 on 2023-02-12 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]