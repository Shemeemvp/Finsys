# Generated by Django 4.2.3 on 2023-11-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0043_paymentitems_invtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bankacc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cheq_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='creditcard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='upi',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
