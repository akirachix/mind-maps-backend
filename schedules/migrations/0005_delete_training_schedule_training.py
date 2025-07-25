# Generated by Django 5.2.3 on 2025-07-22 11:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_remove_schedule_is_active_and_more'),
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Training',
        ),
        migrations.AddField(
            model_name='schedule',
            name='training',
            field=models.ForeignKey(default=89, on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='trainings.training'),
            preserve_default=False,
        ),
    ]
