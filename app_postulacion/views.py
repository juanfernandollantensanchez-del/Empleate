from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Oferta, Postulacion, HojaDeVida

def home(request):
    return render(request, 'app_postulacion/index.html')

def lista_ofertas(request):
    ofertas = Oferta.objects.all().order_by('-fecha_publicacion')
    return render(request, 'app_postulacion/lista_ofertas.html', {'ofertas': ofertas})

def postular_oferta(request, oferta_id):
    oferta = get_object_or_404(Oferta, id=oferta_id)
    
    # Si el usuario no ha iniciado sesión, se toma el usuario de prueba o el primero registrado
    if request.user.is_authenticated:
        usuario = request.user
    else:
        usuario = User.objects.first()
        if not usuario:
            messages.error(request, "No existe un usuario registrado en el sistema.")
            return redirect('lista_ofertas')

    # Validar si el usuario tiene Hoja de Vida
    if not hasattr(usuario, 'hoja_de_vida'):
        messages.error(request, "El sistema no permite la postulación si el usuario no tiene hoja de vida registrada.")
        return redirect('historial_postulaciones')

    postulacion, created = Postulacion.objects.get_or_create(
        usuario=usuario,
        oferta=oferta
    )
    
    if created:
        messages.success(request, f"¡Postulación exitosa a '{oferta.titulo}'!")
    else:
        messages.info(request, "Ya te habías postulado previamente a esta oferta.")
        
    return redirect('historial_postulaciones')

def historial_postulaciones(request):
    # Si no hay sesión iniciada, muestra todas las postulaciones del sistema para pruebas
    if request.user.is_authenticated:
        postulaciones = Postulacion.objects.filter(usuario=request.user).order_by('-fecha_postulacion')
    else:
        postulaciones = Postulacion.objects.all().order_by('-fecha_postulacion')

    return render(request, 'app_postulacion/historial.html', {'postulaciones': postulaciones})