# Generated by Django 5.0.3 on 2024-04-25 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee12app', '0007_alter_prato_preco_promocional'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='descricao_horario',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=20)),
                ('horario_abertura', models.TimeField()),
                ('horario_fechamento', models.TimeField()),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee12app.estabelecimento')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioFuncionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_semana', models.ManyToManyField(to='coffee12app.diasemana')),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee12app.estabelecimento')),
            ],
        ),
    ]