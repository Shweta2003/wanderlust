# Generated by Django 3.0.6 on 2020-06-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='price',
            field=models.IntegerField(default=1000),
        ),
    ]
