# Generated by Django 5.2.3 on 2025-07-22 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='village',
            options={},
        ),
        migrations.RemoveField(
            model_name='village',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='village',
            name='district',
        ),
        migrations.RemoveField(
            model_name='village',
            name='province',
        ),
        migrations.RemoveField(
            model_name='village',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='village',
            name='updated_at',
        ),
    ]
