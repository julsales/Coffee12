from audioop import avg
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.utils import timezone



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

    cafeteria_favorita = models.ManyToManyField('Estabelecimento', blank=True, related_name='cafeterias_favoritas')


    

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    proprietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    descricao_horario = models.CharField(max_length=200, default='')
    @property
    def rating_average(self):
        return self.feedback_set.aggregate(Avg('rating'))['rating__avg']
    
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
    prato_principal = models.BooleanField(default=False)

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cafeteria = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class Historico(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cafeteria = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)

class Reserva(models.Model):
    PENDENTE = 'PE'
    ACEITO = 'AC'
    RECUSADO = 'RE'
    CANCELADO = 'CA'  # Adicione esta linha

    STATUS = [
        (PENDENTE, 'Pendente'),
        (ACEITO, 'Aceito'),
        (RECUSADO, 'Recusado'),
        (CANCELADO, 'Cancelado'),  # Adicione esta linha
    ]

    cafe = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    numero_pessoas = models.IntegerField()
    status = models.CharField(max_length=2, choices=STATUS, default=PENDENTE)

class ItemEsquecido(models.Model):
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cafeteria = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    PENDENTE = 'PE'
    ACHADO = 'AC'
    NAO_ENCONTRADO = 'NE'

    STATUS = [
        (PENDENTE, 'Pendente'),
        (ACHADO, 'Achado'),
        (NAO_ENCONTRADO, 'Não Encontrado'),
    ]

    status = models.CharField(max_length=2, choices=STATUS, default=PENDENTE)

    def __str__(self):
        return self.descricao