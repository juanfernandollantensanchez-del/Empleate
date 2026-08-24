from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import Usuario

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

# VISTA PRINCIPAL (CARGA DIRECTO AL ENTRAR AL LINK)
def inicio(request):
    contexto = {'usuario': request.user}

    if request.user.is_authenticated:
        # Si inició sesión, muestra tablas según su rol
        if request.user.rol == 'admin':
            contexto['todos_usuarios'] = Usuario.objects.all()
        elif request.user.rol == 'empresa':
            contexto['candidatos'] = Usuario.objects.filter(rol='candidato', estado=True)
        elif request.user.rol == 'candidato':
            contexto['empresas'] = Usuario.objects.filter(rol='empresa', estado=True)
    else:
        # Si entra sin iniciar sesión, muestra la información pública
        contexto['candidatos'] = Usuario.objects.filter(rol='candidato', estado=True)
        contexto['empresas'] = Usuario.objects.filter(rol='empresa', estado=True)

    return render(request, 'inicio.html', contexto)

def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('login')

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