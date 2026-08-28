from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import OfertaEmpleo, Postulacion

def lista_ofertas(request):
    """Muestra todas las ofertas activas."""
    ofertas = OfertaEmpleo.objects.filter(activa=True).order_by('-fecha_publicacion')
    return render(request, 'postulacion/lista_ofertas.html', {'ofertas': ofertas})

def detalle_oferta(request, oferta_id):
    """Muestra el detalle de una oferta específica."""
    oferta = get_object_or_404(OfertaEmpleo, id=oferta_id)
    return render(request, 'postulacion/detalle_oferta.html', {'oferta': oferta})

@login_required
def mis_postulaciones(request):
    """Muestra las postulaciones del usuario que ha iniciado sesión."""
    postulaciones = Postulacion.objects.filter(usuario=request.user).order_by('-fecha_postulacion')
    return render(request, 'postulacion/mis_postulaciones.html', {'postulaciones': postulaciones})

@login_required
def postularse(request, oferta_id):
    """Crea una nueva postulación para el usuario autenticado."""
    oferta = get_object_or_404(OfertaEmpleo, id=oferta_id)
    
    # Validar que el usuario no se haya postulado ya
    postulacion_existente = Postulacion.objects.filter(usuario=request.user, oferta=oferta).exists()
    
    if postulacion_existente:
        messages.warning(request, 'Ya te has postulado a esta oferta anteriormente.')
    else:
        # Crear la postulación
        Postulacion.objects.create(usuario=request.user, oferta=oferta)
        messages.success(request, f'Te has postulado exitosamente a: {oferta.titulo}')
        
    return redirect('mis_postulaciones')