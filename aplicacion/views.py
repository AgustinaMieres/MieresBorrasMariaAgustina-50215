from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html") 


#_______________________________________________________________________Forms

#_______________________________________________________________________Libros

def libros(request):
    contexto={'libros':Libro.objects.all().order_by("id")}
    return render(request, "aplicacion/libros.html", contexto)


@login_required
def librosCreate(request):
    
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

            return redirect(reverse_lazy('libros'))     

    else:
    
        miForm = LibrosForm()

    return render(request, "aplicacion/librosForm.html", {"form": miForm} )


#_____________________________________________Codigo para actualizar (update) y eliminar (delete) cosas de mi formulario libros

@login_required
def librosUpdate(request, id_libros):
    libros = Libro.objects.get(id=id_libros)
    if request.method == "POST":
        miForm = LibrosForm(request.POST)
        if miForm.is_valid():
            libros.nombre = miForm.cleaned_data.get("nombre")
            libros.autor = miForm.cleaned_data.get("autor")
            libros.editorial = miForm.cleaned_data.get("editorial")
            libros.genero = miForm.cleaned_data.get("genero")
            libros.precio = miForm.cleaned_data.get("precio")
            libros.save()

            return redirect(reverse_lazy('libros'))

            
            
    else:
        miForm = LibrosForm(initial={'nombre': libros.nombre, 'autor': libros.autor,'editorial': libros.editorial,'genero': libros.genero, 'precio': libros.precio })

    return render(request, "aplicacion/libros.html", {"form": miForm} )

@login_required
def librosDelete(request, id_libros):
    libros = Libro.objects.get(id=id_libros)
    libros.delete()
    return redirect(reverse_lazy('libros'))







#_______________________________________________________________________Libreria


def libreria(request):
    contexto={'libreria':Libreria.objects.all().order_by("id")}
    return render(request, "aplicacion/libreria.html", contexto)

@login_required
def libreriaCreate(request):
    
    if request.method == "POST":
        miForm= LibreriaForm(request.POST)
        if miForm.is_valid():
            libreria_articulo = miForm.cleaned_data.get("articulo")
            libreria_precio = miForm.cleaned_data.get("precio")
            libreria = Libreria(articulo=libreria_articulo, precio=libreria_precio)
            libreria.save()
            
            return redirect(reverse_lazy('libreria'))

    else:
        miForm=LibreriaForm()

    return render (request,"aplicacion/libreriaForm.html", {"form": miForm} )

#_____________________________________________Codigo para actualizar (update) y eliminar (delete) cosas de mi formulario libreria

@login_required
def libreriaUpdate(request, id_libreria):
    libreria = Libreria.objects.get(id=id_libreria)
    if request.method == "POST":
        miForm = LibreriaForm(request.POST)
        if miForm.is_valid():
            libreria.articulo = miForm.cleaned_data.get("articulo")
            libreria.precio = miForm.cleaned_data.get("precio")
            libreria.save()
            return redirect(reverse_lazy('libreria'))
            
            
    else:
        miForm = LibreriaForm(initial={'articulo': libreria.articulo, 'precio': libreria.precio })

    return render(request, "aplicacion/libreria.html", {"form": miForm} )

@login_required
def libreriaDelete(request, id_libreria):
    libreria = Libreria.objects.get(id=id_libreria)
    libreria.delete()
    return redirect(reverse_lazy('libreria'))




#_______________________________________________________________________BestSellers

def bestSeller(request):
    contexto={'bestSeller':BestSeller.objects.all().order_by("id")}
    return render(request, "aplicacion/bestSeller.html", contexto)

@login_required
def bestSellerCreate(request):
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

            return redirect(reverse_lazy('bestSeller'))

    else:
    
        miForm = BestSellerForm()

    return render(request, "aplicacion/bestSellerForm.html", {"form": miForm} )


#_____________________________________________Codigo para actualizar (update) y eliminar (delete) cosas de mi formulario Best Sellers

@login_required
def bestSellerUpdate(request, id_bestSeller):
    bestSeller = BestSeller.objects.get(id=id_bestSeller)
    if request.method == "POST":
        miForm = BestSellerForm(request.POST)
        if miForm.is_valid():
            bestSeller.nombre = miForm.cleaned_data.get("nombre")
            bestSeller.autor = miForm.cleaned_data.get("autor")
            bestSeller.editorial = miForm.cleaned_data.get("editorial")
            bestSeller.genero = miForm.cleaned_data.get("genero")
            bestSeller.precio = miForm.cleaned_data.get("precio")
            bestSeller.save()
            return redirect(reverse_lazy('bestSeller'))
            
    else:
        miForm = BestSellerForm(initial={'nombre': bestSeller.nombre, 'autor': bestSeller.autor,'editorial': bestSeller.editorial,'genero': bestSeller.genero, 'precio': bestSeller.precio })

    return render(request, "aplicacion/bestSeller.html", {"form": miForm} )

@login_required
def bestSellerDelete(request, id_bestSeller):
    bestSeller = BestSeller.objects.get(id=id_bestSeller)
    bestSeller.delete()
    return redirect(reverse_lazy('bestSeller'))

#_______________________________________________________________________Sucursales

def sucursales(request):
    contexto={'sucursales':Sucursal.objects.all().order_by("id")}
    return render(request, "aplicacion/sucursales.html", contexto)

@login_required  
def sucursalesCreate(request):
    if request.method == "POST":
        miForm= SucursalForm(request.POST)
        if miForm.is_valid():
            sucursales_direccion = miForm.cleaned_data.get("direccion")
            sucursales_contacto = miForm.cleaned_data.get("contacto")
            sucursales = Sucursal(direccion=sucursales_direccion, contacto=sucursales_contacto)
            sucursales.save()
            
            contexto={'sucursales':Sucursal.objects.all().order_by("id")}
            return render(request, "aplicacion/sucursales.html", contexto)

    else:
        miForm=SucursalForm()

    return render (request,"aplicacion/sucursalesForm.html", {"form": miForm} )

#_____________________________________________Codigo para actualizar (update) y eliminar (delete) cosas de mi formulario sucursales

@login_required
def sucursalesUpdate(request, id_sucursales):
    sucursales = Sucursal.objects.get(id=id_sucursales)
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursales.direccion = miForm.cleaned_data.get("direccion")
            sucursales.contacto = miForm.cleaned_data.get("contacto")
            sucursales.save()
            return redirect(reverse_lazy('sucursales'))
            
            
    else:
        miForm = SucursalForm(initial={'direccion': sucursales.direccion, 'contacto': sucursales.contacto })

    return render(request, "aplicacion/sucursales.html", {"form": miForm} )

@login_required
def sucursalesDelete(request, id_sucursales):
    sucursales = Sucursal.objects.get(id=id_sucursales)
    sucursales.delete()
    return redirect(reverse_lazy('sucursales'))

    

#________________________ Buscar

@login_required
def buscarLibros(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def encontrarLibros(request):
    return render(request, "aplicacion/buscar.html")

#______________________________________________________________Login

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )


#______________________________________________________________Registro

def registrar(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} ) 
