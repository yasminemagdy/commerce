# Generated by Django 3.1.3 on 2020-12-04 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='model', to='auctions.category'),
        ),
    ]
