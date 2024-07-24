# Generated by Django 5.0.6 on 2024-07-23 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0003_delete_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField()),
                ('venta_fecha', models.DateField()),
                ('venta_monto', models.IntegerField()),
                ('venta_cantidad', models.IntegerField()),
            ],
        ),
    ]
