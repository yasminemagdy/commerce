# Generated by Django 3.1.3 on 2020-12-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20201204_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='close',
            field=models.BooleanField(default=False),
        ),
    ]
