# Generated by Django 3.1.3 on 2020-12-04 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20201204_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='listing_id',
            field=models.IntegerField(default=32),
        ),
    ]
