from django.shortcuts import render, redirect

from Apps.Noticias.models import NoticiasModelo
from Apps.Noticias.forms import NoticiaCrearForm


def articulos_listar(request):
    datos = NoticiasModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'noticias/articulos_listar.html', contexto)


def articulos_crear(request):
    if request.method == "POST":
        form = NoticiaCrearForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articulos_listar')
    else:
        form=NoticiaCrearForm()

    contexto = {'form': form}
    return render(request, 'noticias/articulos_crear.html', contexto)

def articulos_eliminar(request, id):  
    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "POST":
        noticia.delete()
        return redirect('articulos_listar')
    else:
        return render(request, 'noticias/articulos_eliminar.html', {'noticia': noticia})



def articulos_editar(request, id):   
    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "GET":
        form=NoticiaCrearForm(instance=noticia)
    else:
        form=NoticiaCrearForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('articulos_listar')
    contexto = {'form': form}
    return render(request, 'noticias/articulos_editar.html', contexto)