# Generated by Django 3.1.3 on 2020-12-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0071_auto_20201215_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='high',
            field=models.IntegerField(),
        ),
    ]
