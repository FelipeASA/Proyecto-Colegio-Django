from django.urls import path, include

from Apps.Vista.views import *

# importamos de la app ventas

urlpatterns = [
    path('', home, name='home'),
    path('noticias/', noticias, name='noticias'),
    path('eventos/', eventos, name='eventos'),
    path('ver/<int:id>/', articulo_ver, name='articulo_ver'),
   
   
]
