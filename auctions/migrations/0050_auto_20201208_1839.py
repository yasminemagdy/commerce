# Generated by Django 3.1.3 on 2020-12-08 14:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0049_auto_20201208_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
