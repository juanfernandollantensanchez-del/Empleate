from django.db import models


class HojaVida(models.Model):

    direccion = models.CharField(max_length=200)

    educacion = models.TextField()

    soporte_educacion = models.FileField(
        upload_to='soportes/educacion/',
        blank=True,
        null=True
    )

    experiencia_laboral = models.TextField()

    soporte_experiencia = models.FileField(
        upload_to='soportes/experiencia/',
        blank=True,
        null=True
    )

    idiomas = models.CharField(max_length=200)

    antecedentes_penales = models.TextField()

    habilidades = models.TextField()

    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('aprobada', 'Aprobada'),
            ('rechazada', 'Rechazada'),
        ],
        default='pendiente'
    )

    def __str__(self):
        return self.direccion