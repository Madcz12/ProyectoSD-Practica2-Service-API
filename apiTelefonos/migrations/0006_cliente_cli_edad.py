# Generated by Django 4.1.1 on 2022-09-26 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiTelefonos', '0005_cliente_venta'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cli_edad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
