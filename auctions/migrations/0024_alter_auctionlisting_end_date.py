# Generated by Django 5.0.7 on 2024-08-11 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_auctionlisting_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 18, 19, 26, 10, 474431, tzinfo=datetime.timezone.utc)),
        ),
    ]
