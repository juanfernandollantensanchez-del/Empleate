from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_postulante', 'id_entrevistador', 'fecha_registro')
    search_fields = ('id_postulante', 'id_entrevistador')
