# Generated by Django 3.1.3 on 2020-12-08 14:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0048_auto_20201208_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
        migrations.AlterField(
            model_name='bid',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 8, 14, 33, 42, 553391, tzinfo=utc)),
        ),
    ]
