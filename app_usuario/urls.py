from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # Al entrar a la raíz, redirige al login
    path('', lambda request: redirect('login')),
    
    path('login/', views.iniciar_sesion, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registrar_usuario, name='registro_usuario'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    path('gestion/', views.gestionar_usuarios, name='gestion_usuarios'),
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]