# Generated by Django 3.1.3 on 2020-12-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_remove_listing_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category',
            new_name='Category',
        ),
    ]