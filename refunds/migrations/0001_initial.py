# Generated by Django 5.2.4 on 2025-07-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(help_text='Reference to the original payment transaction code, if applicable.', max_length=200, unique=True)),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('REQUESTED', 'Requested'), ('PROCESSING', 'Processing'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('COMPLETED', 'Completed')], default='REQUESTED', max_length=50)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('processed_at', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='Internal notes about the refund process.')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Refund',
                'verbose_name_plural': 'Refunds',
                'ordering': ['-requested_at'],
            },
        ),
    ]
