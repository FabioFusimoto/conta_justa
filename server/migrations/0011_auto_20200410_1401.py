# Generated by Django 3.0.4 on 2020-04-10 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20200410_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='measured_at',
            field=models.DateTimeField(),
        ),
    ]
