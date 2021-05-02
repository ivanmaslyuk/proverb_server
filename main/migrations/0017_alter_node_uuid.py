# Generated by Django 3.2 on 2021-04-19 18:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210419_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, unique=True),
        ),
    ]
