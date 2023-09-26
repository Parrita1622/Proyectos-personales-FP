# Generated by Django 4.1.1 on 2023-09-13 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0032_remove_maestro_proyecto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociarmaterial',
            name='material',
            field=models.ForeignKey(blank=True, limit_choices_to={'estado': 'Activo'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.materiales'),
        ),
    ]