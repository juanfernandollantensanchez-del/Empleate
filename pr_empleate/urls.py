from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Autenticación, registro y página de inicio (raíz del sitio)
    path('', include('app_usuario.urls')),

    # Rutas relativas para los demás módulos
    path('empresas/', include('empresas_app.urls')),
    path('categorias/', include('categorias_app.urls')),
    path('empleate/', include('app_hojaVida.urls')),
    path('postulaciones/', include('app_postulacion.urls')),
    path('feedback/', include('app_feedback.urls')),
]