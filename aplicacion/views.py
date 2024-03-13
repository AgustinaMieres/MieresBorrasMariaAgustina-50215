from django.shortcuts import render

from .models import *
from .forms import * 

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html") 

def libros(request):
    contexto={'libros':Libro.objects.all()}
    return render(request, "aplicacion/libros.html", contexto)

def libreria(request):
    return render(request, "aplicacion/libreria.html")

def bestSeller(request):
    return render(request, "aplicacion/bestSeller.html")

def sucursales(request):
    return render(request, "aplicacion/sucursales.html")


def librosForm(request):
    
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            libros_nombre = miForm.cleaned_data.get("nombre")
            libros_autor = miForm.cleaned_data.get("autor")
            libros_editorial = miForm.cleaned_data.get("editorial")
            libros_genero = miForm.cleaned_data.get("genero")
            libros_precio = miForm.cleaned_data.get("precio")
            libros = Libro(nombre=libros_nombre, autor=libros_autor, editorial=libros_editorial, genero=libros_genero, precio=libros_precio)
            libros.save()

            contexto = {'libros': Libro.objects.all()}
            return render(request, "aplicacion/libros.html", contexto) 

    else:
    
        miForm = LibrosForm()

    return render(request, "aplicacion/librosForm.html", {"form": miForm} )

