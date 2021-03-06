# Generated by Django 3.0.4 on 2020-04-07 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_remove_bill_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=3, max_digits=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.Bill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.User')),
            ],
        ),
    ]
