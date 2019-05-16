from django.urls import path, include

from Apps.Noticias.views import *

# importamos de la app ventas

urlpatterns = [
    path('', articulos_listar, name='articulos_listar'),
    path('crear/', articulos_crear, name='articulos_crear'),
    path('eliminar/<int:id>/', articulos_eliminar, name='articulos_eliminar'),
    path('editar/<int:id>/', articulos_editar, name='articulos_editar'),
   
]
