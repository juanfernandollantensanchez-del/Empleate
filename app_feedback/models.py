from django.db import models

class Feedback(models.Model):
    id_postulante = models.IntegerField(verbose_name="ID del Postulante")
    id_entrevistador = models.IntegerField(verbose_name="ID del Entrevistador")
    comentarios_entrevistador = models.TextField(verbose_name="Comentarios de la Entrevista", blank=True, null=True)
    puntaje_entrevista = models.IntegerField(verbose_name="Puntaje Obtenido", blank=True, null=True)
    resultado_test_diagnostico = models.TextField(verbose_name="Resultados del Test", blank=True, null=True)
    nivel_inicial_detectado = models.CharField(max_length=100, verbose_name="Nivel Inicial Detectado", blank=True, null=True)
    tips_entrenamiento = models.TextField(verbose_name="Tips de Entrenamiento", blank=True, null=True)
    recomendaciones_mejora = models.TextField(verbose_name="Recomendaciones de Mejora", blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def __str__(self):
        return f"Feedback {self.id} - Postulante {self.id_postulante}"
