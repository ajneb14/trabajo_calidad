# Generated by Django 5.0.6 on 2024-06-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_alter_persona_fecha_crea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_crea',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
    ]
