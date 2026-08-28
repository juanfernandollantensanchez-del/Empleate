from django.urls import path
from . import views

urlpatterns = [
    # Al entrar a /crear-empleate/ cargará directamente la vista crear_empleate
    path('', views.crear_empleate, name='crear_empleate'),
    path('multilinea/', views.fnEmpleateMultilinea, name='fn_multilinea'),
    path('vista/', views.fn_empleate, name='fn_empleate'),
]