from django.shortcuts import render, redirect
from Apps.Noticias.models import NoticiasModelo



def home(request):
   
    return render(request, 'vista/home.html',)



def noticias(request):
    datos = NoticiasModelo.objects.filter(tipo = 'noticias')
    contexto = {'lista': datos}
    return render(request, 'vista/noticias.html', contexto)

def eventos(request):
    datos = NoticiasModelo.objects.filter(tipo = 'eventos')
    contexto = {'lista': datos}
    return render(request, 'vista/eventos.html', contexto)

def articulo_ver(request, id):  
    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "POST":
       
        return redirect('noticias')
    else:
        return render(request, 'vista/ver.html', {'noticia': noticia})