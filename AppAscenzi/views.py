from django.shortcuts import render
from AppAscenzi.models import Mayorista, Minorista
from AppAscenzi.forms import MinForm

def index(request):
    return render(request, "AppAscenzi/index.html")

def pedidos(request):
    return render(request, "AppAscenzi/pedidos.html" )

def busqueda(request):
    return render(request, "AppAscenzi/busqueda.html")

def Mayorista_formulario(request):      
    mayoristas = Mayorista.objects.all() 
    return render(request,"AppAscenzi/mayorista.html", {"mayoristas": mayoristas})


def Minorista_formulario(request):   
    context = {
        "form": MinForm(),
        "minoristas": Minorista.objects.all()
    }    
    return render(request,"AppAscenzi/minorista.html", context)

def reset_Minorista(request):
    min_form = MinForm(request.POST)
    min_form.save()
    context = {
        "form": MinForm()
    }
    return render(request, "AppAscenzi/minorista.html", context)