# Generated by Django 5.0.3 on 2024-04-24 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee12app', '0002_alter_customuser_managers_estabelecimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='possui_estabelecimento',
            field=models.BooleanField(default=False),
        ),
    ]
