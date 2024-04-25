from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager



class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    
    COFFEEADMIN = 'CM'
    CLIENT = 'CL'

    ROLES = [
        (COFFEEADMIN, 'Administrador de Café'),
        (CLIENT, 'Cliente')
    ]

    role = models.CharField(
        max_length=2,
        choices=ROLES,
        default=CLIENT,
    )
    cafeteria = models.ForeignKey('Estabelecimento', on_delete=models.PROTECT, null=True, blank=True)

    possui_estabelecimento = models.BooleanField(default=False)


    

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    proprietario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)