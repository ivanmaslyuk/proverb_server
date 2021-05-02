# Generated by Django 3.1.7 on 2021-04-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210319_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='revision',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.node'),
        ),
    ]