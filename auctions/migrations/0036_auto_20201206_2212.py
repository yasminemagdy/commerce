# Generated by Django 3.1.3 on 2020-12-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_pro_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
