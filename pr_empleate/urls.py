from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_usuario.urls')),  # Carga la app de usuario desde la raíz
    path('vacantes/', include('app_empleate.urls')),
    path('empresas/', include('empresas_app.urls')),
    path('categorias/', include('categorias_app.urls')),
    path('empleate/', include('app_hojaVida.urls')),
    path('postulaciones/', include('app_postulacion.urls')),
    path('feedback/', include('app_feedback.urls')),
]