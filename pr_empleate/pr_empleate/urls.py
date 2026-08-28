from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('app_usuario.urls')),
    path('empresas/', include('empresas_app.urls')),
    path('categorias/', include('categorias_app.urls')),
    path('hoja-vida/', include('app_hojaVida.urls')),
]