# Generated by Django 3.1.3 on 2020-11-30 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201130_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='Model',
            new_name='model',
        ),
    ]