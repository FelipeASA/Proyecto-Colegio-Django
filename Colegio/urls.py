from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('/', admin.site.urls),
    path('articulos/', include('Apps.Noticias.urls')),
    path('home/', include('Apps.Vista.urls')),
    
    
]
