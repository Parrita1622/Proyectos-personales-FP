# Generated by Django 4.1.1 on 2023-08-12 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0002_materiales_proyectos_asociados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiales',
            name='proyectos_asociados',
        ),
    ]
