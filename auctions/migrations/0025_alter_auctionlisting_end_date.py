# Generated by Django 5.0.7 on 2024-08-11 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_alter_auctionlisting_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 18, 20, 57, 17, 504497, tzinfo=datetime.timezone.utc)),
        ),
    ]
