# Generated by Django 5.2.4 on 2025-07-19 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_awarded', models.PositiveIntegerField(help_text='Number of points awarded for this specific attendance.')),
                ('awarded_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the reward was created.')),
                ('attendance', models.OneToOneField(help_text='The attendance record that earned this reward.', on_delete=django.db.models.deletion.CASCADE, related_name='reward', to='attendance.attendance')),
            ],
            options={
                'verbose_name': 'Reward',
                'verbose_name_plural': 'Rewards',
                'ordering': ['-awarded_at'],
            },
        ),
    ]
