# Generated by Django 5.0.3 on 2025-03-07 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('pausa', 'En Pausa')], default='activo', max_length=10),
        ),
    ]
