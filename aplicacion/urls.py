from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', home, name="home"),
    path('acerca/', acerca, name="acerca_de_mi"),

    path('libros/', libros, name="libros"),
    path('libros_create/', librosCreate, name="libros_create"),
    path('libros_update/<id_libros>/', librosUpdate, name="libros_update"),
    path('libros_delete/<id_libros>/', librosDelete, name="libros_delete"),

      #___________________ Libreria
    path('libreria/', libreria, name="libreria"),
    path('libreria_create/', libreriaCreate, name="libreria_create"),
    path('libreria_update/<id_libreria>/', libreriaUpdate, name="libreria_update"),
    path('libreria_delete/<id_libreria>/', libreriaDelete, name="libreria_delete"),

      #___________________ BestSeller
    path('bestSeller/', bestSeller, name="bestSeller"),
    path('bestSeller_create/', bestSellerCreate, name="bestSeller_create"),
    path('bestSeller_update/<id_bestSeller>/', bestSellerUpdate, name="bestSeller_update"),
    path('bestSeller_delete/<id_bestSeller>/', bestSellerDelete, name="bestSeller_delete"),

      #___________________ Sucursales
    path('sucursales/', sucursales, name="sucursales"),
    path('sucursales_create/', sucursalesCreate, name="sucursales_create"),
    path('sucursales_update/<id_sucursales>/', sucursalesUpdate, name="sucursales_update"),
    path('sucursaleslibros_delete/<id_sucursaales>/', sucursalesDelete, name="sucursales_delete"),

   
    


    #____________________ Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', registrar, name="registrar"),
    
    #_____________________Edicion perfil
    path('perfil/', editProfile, name="perfil"),


    #_____________________Cambio clave
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),

    #___________________________Avatar
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),


]
