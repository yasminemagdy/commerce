# Generated by Django 3.1.3 on 2020-12-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20201204_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bidder',
            field=models.CharField(default=models.IntegerField(), max_length=64),
        ),
    ]
