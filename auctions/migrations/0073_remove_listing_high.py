# Generated by Django 3.1.3 on 2020-12-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0072_auto_20201215_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='high',
        ),
    ]
