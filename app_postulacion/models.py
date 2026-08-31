from django.db import models
from django.contrib.auth.models import User

class HojaDeVida(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hoja_de_vida')
    titulo_profesional = models.CharField(max_length=150)
    descripcion = models.TextField()

    def __str__(self):
        return f"Hoja de Vida - {self.usuario.username}"

class Oferta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Postulacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='postulaciones')
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='postulaciones')
    fecha_postulacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'oferta') # Evita postulaciones duplicadas a una misma oferta

    def __str__(self):
        return f"{self.usuario.username} -> {self.oferta.titulo}"