# Generated by Django 3.2.22 on 2023-11-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_auto_20231125_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentitems',
            name='invid',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]