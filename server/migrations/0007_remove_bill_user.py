# Generated by Django 3.0.4 on 2020-04-07 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_auto_20200407_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
    ]
