from django.db import models
from django.contrib.auth.models import User

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

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"