# Generated by Django 3.0.6 on 2020-06-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_auto_20200609_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='flights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('From', models.CharField(max_length=200)),
                ('To', models.CharField(max_length=200)),
                ('noof', models.IntegerField()),
                ('price', models.CharField(max_length=400)),
            ],
        ),
    ]
