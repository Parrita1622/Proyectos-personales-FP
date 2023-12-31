# Generated by Django 4.1.1 on 2023-09-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0021_papelerareciclaje_maestro'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='papelerareciclaje',
            name='maestro',
        ),
        migrations.RemoveField(
            model_name='papelerareciclaje',
            name='usuario_que_elimino',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Eliminado', 'Eliminado')], default='Activo', max_length=10),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='PapeleraReciclaje',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
