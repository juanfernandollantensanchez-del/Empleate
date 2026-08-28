from django.shortcuts import render, redirect, get_object_or_404
from .models import OfertaVacante


def inicio(request):
    vacantes = OfertaVacante.objects.all()

    return render(
        request,
        'app_empleate/inicio.html',
        {'vacantes': vacantes}
    )


def crear_vacante(request):
    if request.method == 'POST':
        OfertaVacante.objects.create(
            cargo=request.POST['cargo'],
            categoria=request.POST['categoria'],
            descripcion=request.POST['descripcion'],
            salario=request.POST['salario'],
            empresa=request.POST['empresa']
        )

        return redirect('inicio')

    return render(
        request,
        'app_empleate/crear_vacante.html'
    )


def editar_vacante(request, id):
    vacante = get_object_or_404(OfertaVacante, id=id)

    if request.method == 'POST':
        vacante.cargo = request.POST['cargo']
        vacante.categoria = request.POST['categoria']
        vacante.descripcion = request.POST['descripcion']
        vacante.salario = request.POST['salario']
        vacante.empresa = request.POST['empresa']

        vacante.save()

        return redirect('inicio')

    return render(
        request,
        'app_empleate/editar_vacante.html',
        {'vacante': vacante}
    )


def buscar_vacantes(request):
    vacantes = OfertaVacante.objects.all()

    categoria = request.GET.get('categoria')
    salario_min = request.GET.get('salario_min')
    salario_max = request.GET.get('salario_max')

    if categoria:
        vacantes = vacantes.filter(
            categoria__icontains=categoria
        )

    if salario_min:
        vacantes = vacantes.filter(
            salario__gte=salario_min
        )

    if salario_max:
        vacantes = vacantes.filter(
            salario__lte=salario_max
        )

    return render(
        request,
        'app_empleate/buscar_vacantes.html',
        {'vacantes': vacantes}
    )