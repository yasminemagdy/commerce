# Generated by Django 3.1.3 on 2020-12-07 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20201207_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='close',
            field=models.BooleanField(default=True),
        ),
    ]
