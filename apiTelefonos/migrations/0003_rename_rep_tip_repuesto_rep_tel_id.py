# Generated by Django 4.1.1 on 2022-09-25 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiTelefonos', '0002_telefono_repuesto_rep_precio_repuesto_rep_tip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repuesto',
            old_name='rep_tip',
            new_name='rep_tel_id',
        ),
    ]
