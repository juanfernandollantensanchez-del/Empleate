from django.contrib import admin
from .models import OfertaVacante


@admin.register(OfertaVacante)
class OfertaVacanteAdmin(admin.ModelAdmin):
    list_display = (
        'cargo',
        'categoria',
        'empresa',
        'salario',
        'fecha_publicacion',
    )

    search_fields = (
        'cargo',
        'categoria',
        'empresa',
    )

    list_filter = (
        'categoria',
    )