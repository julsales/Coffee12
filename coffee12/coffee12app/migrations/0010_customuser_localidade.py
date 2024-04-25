# Generated by Django 5.0.3 on 2024-04-25 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee12app', '0009_prato_prato_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='localidade',
            field=models.CharField(choices=[('ZN', 'Zona Norte'), ('ZS', 'Zona Sul'), ('ZO', 'Zona Oeste'), ('CE', 'Centro'), ('NI', 'Não Identificar')], default='NI', max_length=2),
        ),
    ]