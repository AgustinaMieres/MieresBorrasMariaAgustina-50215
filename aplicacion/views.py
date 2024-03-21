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

#_______________________________________________________________________Forms

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
        miForm= LibreriaForm(request.POST)
        if miForm.is_valid():
            libreria_articulo = miForm.cleaned_data.get("articulo")
            libreria_precio = miForm.cleaned_data.get("precio")
            libreria = Libreria(articulo=libreria_articulo, precio=libreria_precio)
            libreria.save()
            
            contexto={'libreria':Libreria.objects.all()}
            return render(request, "aplicacion/libreria.html", contexto)

    else:
        miForm=LibreriaForm()

    return render (request,"aplicacion/libreriaForm.html", {"form": miForm} )

def bestSellerForm(request):
    if request.method == "POST":
        miForm = BestSellerForm(request.POST)
        if miForm.is_valid():
            bestSeller_nombre = miForm.cleaned_data.get("nombre")
            bestSeller_autor = miForm.cleaned_data.get("autor")
            bestSeller_editorial = miForm.cleaned_data.get("editorial")
            bestSeller_genero = miForm.cleaned_data.get("genero")
            bestSeller_precio = miForm.cleaned_data.get("precio")
            bestSeller = BestSeller(nombre=bestSeller_nombre, autor=bestSeller_autor, editorial=bestSeller_editorial, genero=bestSeller_genero, precio=bestSeller_precio)
            bestSeller.save()

            contexto = {'bestSeller': BestSeller.objects.all()}
            return render(request, "aplicacion/bestSeller.html", contexto) 

    else:
    
        miForm = BestSellerForm()

    return render(request, "aplicacion/bestSellerForm.html", {"form": miForm} )

    
def sucursalesForm(request):
    if request.method == "POST":
        miForm= SucursalForm(request.POST)
        if miForm.is_valid():
            sucursales_direccion = miForm.cleaned_data.get("direccion")
            sucursales_contacto = miForm.cleaned_data.get("contacto")
            sucursales = Sucursal(direccion=sucursales_direccion, contacto=sucursales_contacto)
            sucursales.save()
            
            contexto={'sucursales':Sucursal.objects.all()}
            return render(request, "aplicacion/sucursales.html", contexto)

    else:
        miForm=SucursalForm()

    return render (request,"aplicacion/sucursalesForm.html", {"form": miForm} )

    

    
