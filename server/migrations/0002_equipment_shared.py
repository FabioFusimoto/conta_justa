# Generated by Django 3.0.4 on 2020-04-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='shared',
            field=models.BooleanField(default=False),
        ),
    ]
