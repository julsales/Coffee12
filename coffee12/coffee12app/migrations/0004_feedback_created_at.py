# Generated by Django 5.0.3 on 2024-06-07 00:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee12app', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
