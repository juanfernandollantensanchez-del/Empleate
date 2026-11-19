from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Títulos en español para el Panel de Administración (/admin/)
admin.site.site_header = "Administración de Empleate"
admin.site.site_title = "Portal Admin Empleate"
admin.site.index_title = "Panel de Control General (Base de Datos)"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('app_usuario.urls')),
    path('vacantes/', include('app_empleate.urls')),
    path('empresas/', include('empresas_app.urls')),
    path('categorias/', include('categorias_app.urls')),
    path('crear/', include('app_hojaVida.urls')),
    path('postulaciones/', include('app_postulacion.urls')),
    path('feedback/', include('app_feedback.urls')),
]

# Permite servir archivos subidos (como Hojas de Vida) en modo desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)