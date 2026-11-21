from django.urls import path
from . import views  # Importa las vistas locales

urlpatterns = [
    # Mapea directamente la vista, SIN include
    path('', views.crear_empleate, name='crear'),
]