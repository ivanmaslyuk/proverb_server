# Generated by Django 3.1.7 on 2021-04-19 17:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210419_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=32, unique=True),
        ),
    ]