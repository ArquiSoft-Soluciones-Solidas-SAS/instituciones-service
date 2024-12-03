import factory
from bson import ObjectId
from factory import Faker
from .models import Institucion, Curso
import factory.django
from factory.mongoengine import MongoEngineFactory
from faker_education import SchoolProvider

class InstitucionFactory(MongoEngineFactory):
    class Meta:
        model = Institucion

    factory.Faker.add_provider(SchoolProvider)
    nombreInstitucion = Faker('school_name')

    # Usamos LazyAttribute para crear los cursos para cada institución
    cursos = factory.LazyAttribute(lambda o: [
        CursoFactory(grado=grado, numero=numero, anio=2024)
        for grado in ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto', 'Séptimo', 'Octavo', 'Noveno', 'Décimo', 'Undécimo']
        for numero in [1, 2]
    ])

class CursoFactory(MongoEngineFactory):
    class Meta:
        model = Curso

    # Usamos ObjectId() para garantizar que cada curso tenga un id único
    id = factory.LazyFunction(ObjectId)
    grado = factory.Iterator(
        ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto', 'Séptimo', 'Octavo', 'Noveno', 'Décimo', 'Undécimo']
    )
    numero = factory.Iterator([1, 2])  # Solo números 1 y 2
    anio = 2024  # Año fijo 2024

# Crear instituciones con cursos
def crear_instituciones_con_cursos():
    institucion = InstitucionFactory.create_batch(15)
    for inst in institucion:
        print(inst.nombreInstitucion)
