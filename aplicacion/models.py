from django.db import models

# Create your models here.
#Libros,  libreria, best sellers, sucursales

class Libro(models.Model):
    nombre=models.CharField(max_length=100)
    autor=models.CharField(max_length=100)
    editorial=models.CharField(max_length=100)
    genero=models.CharField(max_length=100)
    precio=models.IntegerField()

class Libreria(models.Model):
    articulo=models.CharField(max_length=100)
    precio=models.IntegerField()

class BestSeller(models.Model):
    nombre=models.CharField(max_length=100)
    autor=models.CharField(max_length=100)
    editorial=models.CharField(max_length=100)
    genero=models.CharField(max_length=100)
    precio=models.IntegerField()

class Sucursal(models.Model):
    direccion=models.CharField(max_length=150)
    contacto=models.IntegerField()

