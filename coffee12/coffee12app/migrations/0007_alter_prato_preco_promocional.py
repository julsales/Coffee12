# Generated by Django 5.0.3 on 2024-04-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee12app', '0006_rename_em_promocao_prato_preco_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='preco_promocional',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
