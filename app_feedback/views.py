import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback

@csrf_exempt
def gestionar_feedback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if 'id_postulante' not in data or 'id_entrevistador' not in data:
                return JsonResponse({'status': 'error', 'message': 'IDs obligatorios.'}, status=400)
            
            nuevo_feedback = Feedback.objects.create(
                id_postulante=data['id_postulante'],
                id_entrevistador=data['id_entrevistador'],
                comentarios_entrevistador=data.get('comentarios_entrevistador', ''),
                puntaje_entrevista=data.get('puntaje_entrevista', 0),
                resultado_test_diagnostico=data.get('resultado_test_diagnostico', ''),
                nivel_inicial_detectado=data.get('nivel_inicial_detectado', ''),
                tips_entrenamiento=data.get('tips_entrenamiento', ''),
                recomendaciones_mejora=data.get('recomendaciones_mejora', '')
            )
            return JsonResponse({'status': 'success', 'id_registro': nuevo_feedback.id}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    elif request.method == 'GET':
        registros = list(Feedback.objects.all().values())
        return JsonResponse(registros, safe=False, status=200)

    return JsonResponse({'status': 'error', 'message': 'Método no soportado.'}, status=405)
