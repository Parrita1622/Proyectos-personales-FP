# Generated by Django 4.1.1 on 2023-08-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0004_alter_boleta_observacion_alter_factura_observacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiales',
            name='observacion',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]