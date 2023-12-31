# Generated by Django 4.1.1 on 2023-08-14 23:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cabin_APP', '0007_remove_factura_proyectos_asociados_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsociarFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proyecto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.proyecto')),
                ('numero_factura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.factura')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
