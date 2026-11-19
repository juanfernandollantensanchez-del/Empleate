from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('inicio/', views.inicio, name='inicio'),
    path('login/', views.iniciar_sesion, name='login'),
    path('registro/', views.registrar_usuario, name='registro_usuario'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('cambiar-password/', views.cambiar_password, name='cambiar_password'),
    path('gestion/', views.gestionar_usuarios, name='gestion_usuarios'),
    path('eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('chatbot-ia/', views.chatbot_asistente, name='chatbot_asistente'),
]