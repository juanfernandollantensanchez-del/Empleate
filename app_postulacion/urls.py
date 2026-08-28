from django.urls import path
from . import views

urlpatterns = [
    # Lista de todas las ofertas disponibles
    path('ofertas/', views.lista_ofertas, name='lista_ofertas'),
    
    # Detalle de una oferta específica
    path('ofertas/<int:oferta_id>/', views.detalle_oferta, name='detalle_oferta'),
    
    # Lista de postulaciones del usuario autenticado
    path('mis-postulaciones/', views.mis_postulaciones, name='mis_postulaciones'),
    
    # Acción de postularse a una oferta
    path('postularse/<int:oferta_id>/', views.postularse, name='postularse'),
]