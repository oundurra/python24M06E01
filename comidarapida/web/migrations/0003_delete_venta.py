# Generated by Django 5.0.6 on 2024-07-23 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_ventas_venta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
