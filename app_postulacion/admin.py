from django.contrib import admin
from . models import OfertaEmpleo, HojaVida, Postulacion

@admin.register(OfertaEmpleo)
class OfertaEmpleoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'empresa', 'fecha_publicacion', 'activa']
    list_filter = ['activa', 'empresa']
    search_fields = ['titulo', 'empresa']
    ordering = ['-fecha_publicacion']

@admin.register(HojaVida)
class HojaVidaAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'email', 'telefono', 'fecha_creacion']
    search_fields = ['nombre_completo', 'email']
    ordering = ['-fecha_creacion']

@admin.register(Postulacion)
class PostulacionAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'oferta', 'fecha_postulacion', 'estado']
    list_filter = ['estado', 'fecha_postulacion']
    search_fields = ['usuario__username', 'oferta__titulo']
    ordering = ['-fecha_postulacion']