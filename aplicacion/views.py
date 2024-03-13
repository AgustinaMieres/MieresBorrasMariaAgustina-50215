from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html") 

def libros(request):
    return render(request, "aplicacion/libros.html")

def libreria(request):
    return render(request, "aplicacion/libreria.html")

def bestSeller(request):
    return render(request, "aplicacion/bestSeller.html")

def sucursales(request):
    return sucursales(request, "aplicacion/sucursales.html")
