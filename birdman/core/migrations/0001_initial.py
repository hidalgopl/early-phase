# Generated by Django 2.1.4 on 2019-01-05 17:23

import birdman.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=256)),
                ('address_2', models.CharField(max_length=256)),
                ('zipcode', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHoursDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(validators=[birdman.core.validators.weekday_validator])),
                ('opening', models.TimeField()),
                ('closing', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_created=True)),
                ('photo_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='openinghours',
            name='days',
            field=models.ManyToManyField(to='core.OpeningHoursDaily'),
        ),
    ]
