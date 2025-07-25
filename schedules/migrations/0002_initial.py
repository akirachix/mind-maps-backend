# Generated by Django 5.2.4 on 2025-07-19 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
        ('village', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='extension_worker',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 'Extentionworker'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_schedules', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='schedule',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules', to='village.village'),
        ),
    ]
