# Generated by Django 3.1.7 on 2021-04-19 17:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210419_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 20, 6, 0, 281203)),
        ),
    ]
