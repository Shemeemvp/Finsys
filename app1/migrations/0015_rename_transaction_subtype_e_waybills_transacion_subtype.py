# Generated by Django 4.2.3 on 2023-10-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_e_waybill_item_bill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='e_waybills',
            old_name='transaction_subtype',
            new_name='transacion_subtype',
        ),
    ]
