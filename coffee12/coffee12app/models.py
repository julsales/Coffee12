from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

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

    objects = CustomUserManager()