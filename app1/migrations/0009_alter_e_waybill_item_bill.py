# Generated by Django 4.2.3 on 2023-10-03 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_transportation_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e_waybill_item',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.e_waybills'),
        ),
    ]