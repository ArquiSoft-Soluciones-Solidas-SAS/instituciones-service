from django.urls import path
from . import views

urlpatterns = [
    path('crear-institucion/', views.post, name='crear_institucion'),
    path('listar-instituciones/', views.get, name='listar_instituciones'),
    path('eliminar-instituciones/', views.delete, name='eliminar_instituciones')
]