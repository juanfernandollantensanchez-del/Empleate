import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback

@csrf_exempt
def gestionar_feedback(request):
    """
    Controlador para el Módulo de Diagnóstico y Feedback.
    Maneja el registro (POST) y la consulta (GET) de la tabla feedback.
    """
    # 1. Guardar Feedback (POST)
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Validamos que vengan los IDs obligatorios para enlazar las tablas del proyecto
            if 'id_postulante' not in data or 'id_entrevistador' not in data:
                return JsonResponse({
                    'status': 'error', 
                    'message': 'Los campos id_postulante e id_entrevistador son obligatorios.'
                }, status=400)
            
            # Creamos el registro mapeando cada requerimiento asignado
            nuevo_feedback = Feedback.objects.create(
                id_postulante=data['id_postulante'],
                id_entrevistador=data['id_entrevistador'],
                
                # RF-NU-013: Retroalimentación dada por los entrevistadores
                comentarios_entrevistador=data.get('comentarios_entrevistador', ''),
                puntaje_entrevista=data.get('puntaje_entrevista', 0),
                
                # RF-NU-007: Test de entrevista inicial de diagnóstico
                resultado_test_diagnostico=data.get('resultado_test_diagnostico', ''),
                nivel_inicial_detectado=data.get('nivel_inicial_detectado', ''),
                
                # RF-NU-008, RF-NU-014: Recomendaciones de entrenamiento y tips
                tips_entrenamiento=data.get('tips_entrenamiento', ''),
                recomendaciones_mejora=data.get('recomendaciones_mejora', '')
            )
            
            return JsonResponse({
                'status': 'success',
                'message': 'Módulo de feedback procesado con éxito.',
                'id_registro': nuevo_feedback.id
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'JSON inválido.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # 2. Consultar Feedbacks (GET)
    elif request.method == 'GET':
        # Retorna todos los registros guardados en formato de lista JSON
        registros = list(Feedback.objects.all().values())
        return JsonResponse(registros, safe=False, status=200)

    # Si usan otro método HTTP (PUT, DELETE, etc.) que no hemos mapeado aún
    return JsonResponse({'status': 'error', 'message': 'Método HTTP no soportado.'}, status=405)
