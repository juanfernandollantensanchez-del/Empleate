from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    ROLES = (
        ('candidato', 'Candidato'),
        ('empresa', 'Empresa'),
        ('admin', 'Administrador'),
    )
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    profesion_oficio = models.CharField(max_length=150, blank=True, null=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='candidato')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"