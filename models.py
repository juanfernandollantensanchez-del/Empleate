from django.db import models


class OfertaVacante(models.Model):
    cargo = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.CharField(max_length=150)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'ofertas_vacantes'

    def __str__(self):
        return self.cargo