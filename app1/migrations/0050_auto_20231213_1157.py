# Generated by Django 3.2.22 on 2023-12-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0049_auto_20231208_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtable',
            name='min_stock',
            field=models.CharField(default='0', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='file',
            field=models.FileField(default='default.jpg', upload_to='sales'),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='gstnumber',
            field=models.CharField(default='NULL', max_length=150),
        ),
        migrations.AddField(
            model_name='purchasedebit',
            name='gsttype',
            field=models.CharField(default='NULL', max_length=150),
        ),
    ]
