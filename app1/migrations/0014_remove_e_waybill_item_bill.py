# Generated by Django 4.2.3 on 2023-10-03 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_transacion_subtype_e_waybills_transaction_subtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='e_waybill_item',
            name='bill',
        ),
    ]