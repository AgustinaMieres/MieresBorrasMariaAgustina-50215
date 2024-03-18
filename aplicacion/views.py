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
    contexto={'libreria':Libreria.objects.all()}
    return render(request, "aplicacion/libreria.html", contexto)


def bestSeller(request):
    contexto={'bestSeller':BestSeller.objects.all()}
    return render(request, "aplicacion/bestSeller.html", contexto)

def sucursales(request):
    contexto={'sucursales':Sucursal.objects.all()}
    return render(request, "aplicacion/sucursales.html", contexto)


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


def libreriaForm(request):
    
    if request.method == "POST":
        miForm = LibreriaForm(request.POST)
        if miForm.is_valid():
            libreria_articulo = miForm.cleaned_data.get("articulo")
            libreria_precio = miForm.cleaned_data.get("precio")
            
            libreria = Libreria(articulo=libreria_articulo, precio=libreria_precio)
            libreria.save()

            contexto = {'libreria': Libreria.objects.all()}
            return render(request, "aplicacion/libreria.html", contexto) 

    else:
    
        miForm = LibreriaForm()

    return render(request, "aplicacion/libreriaForm.html", {"form": miForm} )

