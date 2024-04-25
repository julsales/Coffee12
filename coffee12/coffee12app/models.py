from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    
    COFFEEADMIN = 'CM'
    CLIENT = 'CL'
    ZONANORTE = 'ZN'
    ZONASUL = 'ZS'
    ZONAOESTE = 'ZO'
    CENTRO = 'CE'
    NAOIDENTIFICAR = 'NI'

    ROLES = [
        (COFFEEADMIN, 'Administrador de Café'),
        (CLIENT, 'Cliente')
    ]

    LOCALIDADES = [
        (ZONANORTE, 'Zona Norte'),
        (ZONASUL, 'Zona Sul'),
        (ZONAOESTE, 'Zona Oeste'),
        (CENTRO, 'Centro'),
        (NAOIDENTIFICAR, 'Não Identificar')
    ]
    role = models.CharField(
        max_length=2,
        choices=ROLES,
        default=CLIENT,
    )
    
    localidade = models.CharField(
        max_length=2,
        choices=LOCALIDADES,
        default=NAOIDENTIFICAR,
    )
    cafeteria = models.ForeignKey('Estabelecimento', on_delete=models.PROTECT, null=True, blank=True)

    possui_estabelecimento = models.BooleanField(default=False)


    

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    proprietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao_horario = models.CharField(max_length=200, default='')
    
class DiaSemana(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    
class HorarioFuncionamento(models.Model):
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    dias_semana = models.ManyToManyField(DiaSemana)

class Prato(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=6, decimal_places=2)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    prato_principal = models.BooleanField(default=False);
    