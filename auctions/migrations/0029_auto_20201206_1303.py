# Generated by Django 3.1.3 on 2020-12-06 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_auto_20201206_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='model',
            field=models.CharField(default=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='auctions.category'), max_length=64),
        ),
    ]
