from bson import ObjectId
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Institucion, Curso
from .utils import send_to_rabbitmq

@csrf_exempt
def post(request):
        # Datos de ejemplo para una institución y cursos
        curso1 = Curso(id=ObjectId(), grado="Primero", numero=1, anio=2024)
        curso2 = Curso(id=ObjectId(), grado="Segundo", numero=2, anio=2024)

        institucion = Institucion(
            nombreInstitucion="Institución de Prueba",
            cursos=[curso1, curso2]
        )
        institucion.save()
        send_to_rabbitmq(
            exchange='instituciones',
            routing_key='institucion.created',
            message={
                "type": "institucion_created",
                "data": {
                    "id": str(institucion.id),
                    "nombreInstitucion": institucion.nombreInstitucion,
                    "cursos": [
                        {"id": str(curso.id),
                         "grado": curso.grado,
                         "numero": curso.numero,
                         "anio": curso.anio}
                        for curso in institucion.cursos
                    ]
                }
            }
        )

        return JsonResponse({
            "mensaje": "Institución creada exitosamente",
            "institucion": institucion.nombreInstitucion
        })


@csrf_exempt
def get(request):
        instituciones = Institucion.objects.all()
        resultado = []
        for institucion in instituciones:
            resultado.append({
                "id": str(institucion.id),
                "nombreInstitucion": institucion.nombreInstitucion,
                "cursos": [
                    {
                        "id": str(curso.id),
                        "grado": curso.grado,
                        "numero": curso.numero,
                        "anio": curso.anio
                    }
                    for curso in institucion.cursos
                ]
            })
        return JsonResponse({"instituciones": resultado})

@csrf_exempt
def delete(request):
        Institucion.objects.all().delete()
        return JsonResponse({"mensaje": "Todas las instituciones han sido eliminadas"})