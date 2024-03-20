from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('libros/', libros, name="libros"),
    path('libreria/', libreria, name="libreria"),
    path('bestSeller/', bestSeller, name="bestSeller"),
    path('sucursales/', sucursales, name="sucursales"),

    #___________________ Formularios
    path('libros_form/', librosForm, name="libros_form"),
    path('libreria_form/', libreriaForm, name="libreria_form"),
]