from django import forms

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