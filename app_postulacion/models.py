from django.db import models
from django.conf import settings

class OfertaEmpleo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    empresa = models.CharField(max_length=100)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class HojaVida(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    experiencia = models.TextField()
    educacion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hoja de vida de {self.nombre_completo}"

class Postulacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    oferta = models.ForeignKey(OfertaEmpleo, on_delete=models.CASCADE)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('REVISADO', 'Revisado'),
            ('ACEPTADO', 'Aceptado'),
            ('RECHAZADO', 'Rechazado')
        ],
        default='PENDIENTE'
    )

    class Meta:
        unique_together = ['usuario', 'oferta']

    def __str__(self):
        return f"{self.usuario.username} - {self.oferta.titulo}"