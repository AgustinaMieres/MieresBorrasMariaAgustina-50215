from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LibrosForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    autor=forms.CharField(max_length=100, required=True)
    editorial=forms.CharField(max_length=100, required=True)
    genero=forms.CharField(max_length=100, required=True)
    precio=forms.IntegerField(required=True)

class LibreriaForm (forms.Form):
    articulo=forms.CharField(max_length=100, required=True)
    precio=forms.IntegerField(required=True)

class BestSellerForm(forms.Form):
    nombre=forms.CharField(max_length=100, required=True)
    autor=forms.CharField(max_length=100, required=True)
    editorial=forms.CharField(max_length=100, required=True)
    genero=forms.CharField(max_length=100, required=True)
    precio=forms.IntegerField(required=True)

class SucursalForm(forms.Form):
    direccion=forms.CharField(max_length=150, required=True)
    contacto=forms.IntegerField(required=True)

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    id_empleado = forms.CharField(label="ID empleado", max_length=100)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "id_empleado")