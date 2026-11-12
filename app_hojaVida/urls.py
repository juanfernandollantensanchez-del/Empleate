from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.crear_empleate
    ),

  

    path(
        'fnEmpleate-Multilinea/',
        views.fnEmpleateMultilinea
    ),

    path(
        'fn-empleate/',
        views.fn_empleate
    ),

]