from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_vacante, name='crear_vacante'),
    path('editar/<int:id>/', views.editar_vacante, name='editar_vacante'),
    path('buscar/', views.buscar_vacantes, name='buscar_vacantes'),
]