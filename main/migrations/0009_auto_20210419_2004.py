# Generated by Django 3.1.7 on 2021-04-19 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210419_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='node',
            old_name='tag',
            new_name='pointer',
        ),
        migrations.AlterField(
            model_name='node',
            name='edited_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 20, 4, 56, 156823)),
        ),
    ]