# Generated by Django 2.1.4 on 2019-02-23 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowork', '0002_auto_20190120_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cowork',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='cowork',
            name='lon',
        ),
    ]
