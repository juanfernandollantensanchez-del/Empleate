from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50, unique=True)
    representante = models.CharField(max_length=150)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nombre