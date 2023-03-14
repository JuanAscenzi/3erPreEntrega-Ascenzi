from django.shortcuts import render
from AppAscenzi.models import Mayorista, Minorista, Pedido
from AppAscenzi.forms import  MayForm, MinForm, PedForm

def index(request):
    return render(request, "AppAscenzi/index.html")

def pedidos(request):
    return render(request, "AppAscenzi/pedidos.html" )

def busqueda(request):
    return render(request, "AppAscenzi/busqueda.html")

def buscar_minorista(request):
    criterio = request.GET.get("criterio")
    context = { "minoristas": Minorista.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "AppAscenzi/busqueda.html", context)

def buscar_mayorista(request):
    criterio = request.GET.get("criterio")
    context = { "mayoristas": Mayorista.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "AppAscenzi/busqueda.html", context)

def buscar_pedido(request):
    criterio = request.GET.get("criterio")
    context = { "pedidos": Pedido.objects.filter(nombre__icontains=criterio).all(),
            }
    return render(request, "AppAscenzi/busqueda.html", context)


def Mayorista_formulario(request):      
    context = {
        "form": MayForm(),
        "mayoristas": Mayorista.objects.all()
    }    
    return render(request,"AppAscenzi/mayorista.html", context)

def Minorista_formulario(request):   
    context = {
        "form": MinForm(),
        "minoristas": Minorista.objects.all()
    }    
    return render(request,"AppAscenzi/minorista.html", context)

def Pedidos_formulario(request):      
    context = {
        "form": PedForm(),
        "pedidos": Pedido.objects.all()
    }    
    return render(request,"AppAscenzi/pedidos.html", context)

def reset_Minorista(request):
    min_form = MinForm(request.POST)
    min_form.save()
    context = {
        "form": MinForm(),
        "minoristas": Minorista.objects.all()
    }
    return render(request, "AppAscenzi/minorista.html", context)

def reset_Mayorista(request):
    may_form = MayForm(request.POST)
    may_form.save()
    context = {
        "form": MayForm(),
        "mayoristas": Mayorista.objects.all()
    }
    return render(request, "AppAscenzi/mayorista.html", context)

def reset_Pedido(request):
    ped_form = PedForm(request.POST)
    ped_form.save()
    context = {
        "form": PedForm(),
        "pedidos": Pedido.objects.all()
    }
    return render(request, "AppAscenzi/pedidos.html", context)