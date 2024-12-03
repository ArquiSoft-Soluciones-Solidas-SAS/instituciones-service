from django.urls import path
from . import views

urlpatterns = [
    path('instituciones/crear-institucion/', views.post, name='crear_institucion'),
    path('instituciones/listar-instituciones/', views.get, name='listar_instituciones'),
    path('instituciones/eliminar-instituciones/', views.delete, name='eliminar_instituciones')
]