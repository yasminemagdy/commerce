# Generated by Django 3.1.3 on 2020-12-07 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0041_auto_20201207_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=64),
        ),
    ]
