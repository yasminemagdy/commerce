# Generated by Django 3.1.3 on 2020-12-08 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0059_auto_20201209_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid',
            field=models.IntegerField(default=int),
        ),
    ]
