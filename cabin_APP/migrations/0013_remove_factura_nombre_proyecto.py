# Generated by Django 4.1.1 on 2023-08-20 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0012_asociarboleta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='nombre_proyecto',
        ),
    ]
