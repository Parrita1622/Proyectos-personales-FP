# Generated by Django 4.1.1 on 2023-09-08 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0018_maestro_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='papelerareciclaje',
            name='usuario_que_elimino',
        ),
    ]
