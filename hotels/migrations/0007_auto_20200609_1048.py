# Generated by Django 3.0.6 on 2020-06-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0006_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='ratings',
            field=models.CharField(max_length=20),
        ),
    ]
