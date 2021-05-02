# Generated by Django 3.1.7 on 2021-04-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210408_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='request',
            name='node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='main.node'),
        ),
    ]
