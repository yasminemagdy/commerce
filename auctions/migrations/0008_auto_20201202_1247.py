# Generated by Django 3.1.3 on 2020-12-02 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201130_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='Bid',
            new_name='bid',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='Holder',
            new_name='holder',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='List_id',
            new_name='list_id',
        ),
        migrations.RenameField(
            model_name='bid',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Holder',
            new_name='holder',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='List_id',
            new_name='list_id',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Holder',
            new_name='holder',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Link',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Model',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='Explnation',
            new_name='txplnation',
        ),
    ]