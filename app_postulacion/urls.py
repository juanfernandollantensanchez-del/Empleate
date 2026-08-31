from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página principal de la app
    path('ofertas/', views.lista_ofertas, name='lista_ofertas'),
    path('postular/<int:oferta_id>/', views.postular_oferta, name='postular_oferta'),
    path('mis-postulaciones/', views.historial_postulaciones, name='historial_postulaciones'),
]