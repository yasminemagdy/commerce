# Generated by Django 3.1.3 on 2020-12-18 12:11

import auctions.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0082_auto_20201217_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bidder',
            field=models.CharField(default=auctions.models.User, max_length=64),
        ),
    ]
