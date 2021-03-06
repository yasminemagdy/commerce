# Generated by Django 3.1.3 on 2020-12-09 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0063_auto_20201209_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winner',
            name='winner',
        ),
        migrations.AddField(
            model_name='winner',
            name='winner_id',
            field=models.IntegerField(default=int),
        ),
        migrations.AlterField(
            model_name='listing',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model', to='auctions.category'),
        ),
    ]
