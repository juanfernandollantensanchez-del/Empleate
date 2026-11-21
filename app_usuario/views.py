import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Usuario
from app_empleate.models import OfertaVacante


# PORTADA PÚBLICA (INSTRUCCIONES, INTEGRANTES Y CHATBOT IA)
def portada(request):
    return render(request, 'portada.html')


@csrf_exempt
def chatbot_asistente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            mensaje = data.get('mensaje', '').lower().strip()
        except Exception:
            mensaje = ''

        if any(p in mensaje for p in ['hola', 'buenos', 'buenas', 'saludos', 'ey']):
            respuesta = (
                "¡Hola! Soy el Asistente Virtual de **Empleate**. Puedo explicarte cómo registrarte, "
                "cómo subir tu Hoja de Vida, cómo postularte a vacantes o cómo funciona el módulo de Empresas. ¿En qué te ayudo?"
            )
        elif any(p in mensaje for p in ['registrar', 'registro', 'cuenta', 'iniciar', 'login', 'entrar']):
            respuesta = (
                "Para ingresar, haz clic en **'Ir a la Plataforma'** en la parte superior. "
                "Desde allí podrás iniciar sesión o crear tu cuenta seleccionando tu rol (**Candidato** o **Empresa**)."
            )
        elif any(p in mensaje for p in ['vacante', 'oferta', 'empleo', 'trabajo', 'postular']):
            respuesta = (
                "En el módulo de **Vacantes** encuentras todas las ofertas laborales activas. "
                "Una vez inicies sesión como candidato, entra a la oferta de tu interés y haz clic en **'Postularme'**."
            )
        elif any(p in mensaje for p in ['hoja de vida', 'cv', 'curriculum', 'perfil']):
            respuesta = (
                "Cuando inicies sesión, dirígete a **'Hoja de Vida'** para registrar tu formación académica, "
                "experiencia y habilidades profesionales."
            )
        elif any(p in mensaje for p in ['empresa', 'reclutar', 'publicar']):
            respuesta = (
                "El módulo de **Empresas** permite registrar organizaciones con su NIT, representante legal "
                "y correo de contacto para publicar vacantes y revisar postulados."
            )
        elif any(p in mensaje for p in ['categoria', 'categoría', 'sector']):
            respuesta = (
                "Las **Categorías** organizan las ofertas de empleo por áreas profesionales para que encuentres "
                "vacantes acordes a tu perfil más rápido."
            )
        elif any(p in mensaje for p in ['integrante', 'creador', 'equipo', 'desarrollador', 'quienes']):
            respuesta = (
                "El equipo creador de **Empleate** está conformado por: Angela Quiñonez, Felipe Escobar, "
                "Santiago Méndez, Juan Sanchez, Jhamilton Arteaga, Florería Silva y Yeison Pino."
            )
        else:
            respuesta = (
                "Puedo orientarte sobre cualquier función de **Empleate**:\n"
                "1️⃣ **Registro e Inicio de Sesión** (Candidato / Empresa)\n"
                "2️⃣ **Hoja de Vida**\n"
                "3️⃣ **Vacantes y Postulaciones**\n"
                "4️⃣ **Empresas, Categorías y Feedback**\n\n"
                "Escríbeme tu pregunta (por ejemplo: *'¿Cómo me postulo?'* o *'¿Cómo creo mi cuenta?'*)."
            )

        return JsonResponse({'respuesta': respuesta})

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado con éxito.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}')
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


def acceso_rapido(request):
    if request.method == 'POST':
        metodo = request.POST.get('metodo', 'telefono')
        dato = request.POST.get('dato_contacto', '').strip()
        rol = request.POST.get('rol', 'candidato')

        if not dato:
            messages.error(request, 'Por favor ingresa tu correo o número de teléfono.')
            return redirect('login')

        if metodo == 'telefono':
            usuario = Usuario.objects.filter(telefono=dato).first()
            if not usuario:
                username_base = f"tel_{dato}"
                usuario, _ = Usuario.objects.get_or_create(
                    username=username_base,
                    defaults={
                        'first_name': 'Usuario',
                        'last_name': dato,
                        'telefono': dato,
                        'rol': rol,
                        'estado': True,
                    }
                )
        else:
            usuario = Usuario.objects.filter(email=dato).first()
            if not usuario:
                nombre_base = dato.split('@')[0]
                usuario, _ = Usuario.objects.get_or_create(
                    username=nombre_base,
                    defaults={
                        'first_name': nombre_base.capitalize(),
                        'last_name': f'({metodo.capitalize()})',
                        'email': dato,
                        'rol': rol,
                        'estado': True,
                    }
                )

        login(request, usuario)
        messages.success(request, f'¡Bienvenido {usuario.first_name}! Ingresaste con {metodo.capitalize()}.')
        return redirect('inicio')

    return redirect('login')


# VISTA PRINCIPAL (ACCESIBLE CON O SIN SESIÓN INICIADA)
def inicio(request):
    contexto = {
        'usuario': request.user,
        'vacantes': OfertaVacante.objects.all().order_by('-id'),
    }

    if request.user.is_authenticated:
        if request.user.rol == 'admin':
            contexto['todos_usuarios'] = Usuario.objects.all()
        elif request.user.rol == 'empresa':
            contexto['candidatos'] = Usuario.objects.filter(rol='candidato', estado=True)
        elif request.user.rol == 'candidato':
            contexto['empresas'] = Usuario.objects.filter(rol='empresa', estado=True)
    else:
        contexto['candidatos'] = Usuario.objects.filter(rol='candidato', estado=True)
        contexto['empresas'] = Usuario.objects.filter(rol='empresa', estado=True)

    return render(request, 'inicio.html', contexto)


def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('portada')


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Contraseña actualizada con éxito.')
            return redirect('inicio')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/cambiar_password.html', {'form': form})


@login_required
def gestionar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/gestion.html', {'usuarios': usuarios})


@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('gestion_usuarios')