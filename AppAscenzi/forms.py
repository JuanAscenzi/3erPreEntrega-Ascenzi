from django import forms
 
class Venta_mayorista(forms.Form):
    nombre = forms.CharField()
    apellido = forms.IntegerField()
