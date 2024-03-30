from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "aplicacion/index.html") 

def acerca(request):
    return render(request, "aplicacion/acerca.html") 


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

    

#________________________ Buscar libros

def buscarLibros(request):
    return render(request, "aplicacion/buscar.html")

def encontrarLibros(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libros = Libro.objects.filter(nombre__icontains=patron)
        contexto = {"libros": libros}
        return render(request, "aplicacion/libros.html", contexto)
    

    contexto = {'libros': Libro.objects.all()}
    return render(request, "aplicacion/libros.html", contexto) 

#________________________ Buscar libreria

def buscarLibreria(request):
    return render(request, "aplicacion/buscarArticulo.html")

def encontrarLibreria(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        libreria = Libreria.objects.filter(articulo__icontains=patron)
        contexto = {"libreria": libreria}
        return render(request, "aplicacion/libreria.html", contexto)
    

    contexto = {'libreria': Libreria.objects.all()}
    return render(request, "aplicacion/libreria.html", contexto) 

#________________________ Buscar Best Seller

def buscarbestSeller(request):
    return render(request, "aplicacion/buscarBestSeller.html")

def encontrarbestSeller(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        bestSeller = BestSeller.objects.filter(nombre__icontains=patron)
        contexto = {"bestSeller": bestSeller}
        return render(request, "aplicacion/bestSeller.html", contexto)
    

    contexto = {'bestSeller': BestSeller.objects.all()}
    return render(request, "aplicacion/bestSeller.html", contexto) 

#________________________ Buscar Sucursal

def buscarSucursal(request):
    return render(request, "aplicacion/buscarSucursal.html")

def encontrarSucursal(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        sucursal = Sucursal.objects.filter(direccion__icontains=patron)
        contexto = {"sucursal": sucursal}
        return render(request, "aplicacion/sucursales.html", contexto)
    

    contexto = {'sucursal': Sucursal.objects.all()}
    return render(request, "aplicacion/sucursales.html", contexto) 






#______________________________________________________________Login

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #______ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            #________________________________________________________


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


#________________________ Edición de Perfil

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
    
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )   


#____________________________Cambio clave

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")


#_________________________________Agregar avatar
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)

            #___ Para borrar el avatar viejo:
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            #____________________________________________________
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )      