# Generated by Django 3.1.3 on 2020-12-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0078_auto_20201217_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bidder',
            field=models.CharField(max_length=64),
        ),
    ]
