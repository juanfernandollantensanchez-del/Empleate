from django.urls import path
from . import views

urlpatterns = [
    # Esta ruta servirá tanto para ver la lista (GET) como para guardar datos (POST)
    path('', views.gestionar_feedback, name='gestionar_feedback'),
]
