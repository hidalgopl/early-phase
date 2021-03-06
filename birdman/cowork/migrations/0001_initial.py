# Generated by Django 2.1.4 on 2019-01-05 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cowork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('capacity', models.IntegerField()),
                ('current_capacity', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Address')),
                ('current_coworkers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_friendly', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('shower', models.BooleanField(default=False)),
                ('ping_pong', models.BooleanField(default=False)),
                ('chill_room', models.BooleanField(default=False)),
                ('free_snack', models.BooleanField(default=False)),
                ('conference_rooms', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MealOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='cowork',
            name='facilities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowork.Facilities'),
        ),
        migrations.AddField(
            model_name='cowork',
            name='opening_hours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.OpeningHours'),
        ),
    ]
