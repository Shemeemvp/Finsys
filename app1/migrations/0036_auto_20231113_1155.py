# Generated by Django 3.2.22 on 2023-11-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20231113_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bill',
            name='profile_name',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recurring_bill',
            name='purchase_order',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]