# Generated by Django 3.1 on 2020-09-12 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(default=' ', max_length=50)),
                ('model', models.CharField(default=' ', max_length=50)),
                ('VIN', models.PositiveBigIntegerField(default=' ')),
                ('DatePurchase', models.DateTimeField()),
                ('LastService', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
        ),
    ]
