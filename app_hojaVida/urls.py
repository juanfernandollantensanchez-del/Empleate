from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [

    path(
        'crear-empleate/',
        views.crear_empleate
    ),

    path(
        '',
        lambda request: HttpResponse(
            "<h1>Bienvenido a mi aplicación EMPLEATE</h1>"
        )
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