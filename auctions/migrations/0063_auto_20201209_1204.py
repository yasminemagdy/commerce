# Generated by Django 3.1.3 on 2020-12-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0062_auto_20201209_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.IntegerField(default=int),
        ),
    ]