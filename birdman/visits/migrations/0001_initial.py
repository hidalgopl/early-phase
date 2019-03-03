# Generated by Django 2.1.5 on 2019-03-03 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cowork', '0003_auto_20190223_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('PENDING', 'PENDING'), ('CONFIRMED', 'CONFIRMED'), ('DECLINED', 'DECLINED')], default='PENDING', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('cowork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cowork.Cowork')),
                ('requesting_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
