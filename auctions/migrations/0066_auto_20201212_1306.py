# Generated by Django 3.1.3 on 2020-12-12 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0065_auto_20201209_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.IntegerField(),
        ),
    ]