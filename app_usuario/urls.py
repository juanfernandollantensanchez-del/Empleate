from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('inicio')),
    path('inicio/', views.inicio, name='inicio'), # <-- Nueva ruta de inicio
    path('registro/', views.registrar_usuario, name='registro_usuario'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    path('gestion/', views.gestionar_usuarios, name='gestion_usuarios'),
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]