# Generated by Django 3.1.3 on 2020-12-08 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0050_auto_20201208_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='winner',
            field=models.IntegerField( default=0)
        ),
    ]
