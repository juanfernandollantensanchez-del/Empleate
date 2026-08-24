from django.shortcuts import render
from .models import HojaVida
from django.http import HttpResponse


def crear_empleate(request):

    if request.method == 'POST':

        direccion = request.POST.get('direccion')
        educacion = request.POST.get('educacion')
        experiencia_laboral = request.POST.get('experiencia_laboral')
        idiomas = request.POST.get('idiomas')
        antecedentes_penales = request.POST.get('antecedentes_penales')
        habilidades = request.POST.get('habilidades')

        soporte_educacion = request.FILES.get('soporte_educacion')
        soporte_experiencia = request.FILES.get('soporte_experiencia')

        # Validar que todos los campos estén diligenciados
        if not direccion or not educacion or not experiencia_laboral or not idiomas or not antecedentes_penales or not habilidades:
            return HttpResponse(
                "<h1>Error</h1>"
                "<p>Todos los campos son obligatorios.</p>"
                "<a href='/crear-empleate/'>Volver al formulario</a>"
            )

        # Validar que existan los soportes
        if not soporte_educacion or not soporte_experiencia:
            return HttpResponse(
                "<h1>Error</h1>"
                "<p>Debes adjuntar los soportes de educación y experiencia laboral.</p>"
                "<a href='/crear-empleate/'>Volver al formulario</a>"
            )

        # Validar que los soportes sean PDF
        if not soporte_educacion.name.lower().endswith('.pdf'):
            return HttpResponse(
                "<h1>Error</h1>"
                "<p>El soporte de educación debe estar en formato PDF.</p>"
                "<a href='/crear-empleate/'>Volver al formulario</a>"
            )

        if not soporte_experiencia.name.lower().endswith('.pdf'):
            return HttpResponse(
                "<h1>Error</h1>"
                "<p>El soporte de experiencia debe estar en formato PDF.</p>"
                "<a href='/crear-empleate/'>Volver al formulario</a>"
            )

        # Guardar hoja de vida
        HojaVida.objects.create(
            direccion=direccion,
            educacion=educacion,
            soporte_educacion=soporte_educacion,
            experiencia_laboral=experiencia_laboral,
            soporte_experiencia=soporte_experiencia,
            idiomas=idiomas,
            antecedentes_penales=antecedentes_penales,
            habilidades=habilidades
        )

        return HttpResponse(
            "<h1>Hoja de vida registrada correctamente</h1>"
            "<p>Tu hoja de vida quedó pendiente de revisión.</p>"
            "<a href='/crear-empleate/'>Registrar otra hoja de vida</a>"
        )

    return render(request, 'registro_hoja_vida.html')


def fnEmpleateMultilinea(request):

    htmlEmpleateMultilinea = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>EMPLEATE</title>
    </head>

    <body>

        <h1>EMPLEATE</h1>

        <p>Busca tu próxima oportunidad laboral</p>

        <input type="text" placeholder="Buscar empleo">

        <button>Buscar</button>

        <h2>Ofertas disponibles</h2>

        <p>Desarrollador Web - Bogotá</p>
        <p>Diseñador Gráfico - Bogotá</p>

    </body>
    </html>
    """

    return HttpResponse(htmlEmpleateMultilinea)


def fn_empleate(request):
    return render(request, 'empleate.html')



