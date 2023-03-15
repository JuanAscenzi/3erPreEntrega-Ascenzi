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
    context = { "minoristas": Minorista.objects.filter(nombre__icontains=criterio)}
    return render(request, "AppAscenzi/busqueda.html", context)

def buscar_mayorista(request):
    criterio = request.GET.get("criterio")
    context = { "mayoristas": Mayorista.objects.filter(nombre__icontains=criterio)}
    return render(request, "AppAscenzi/busqueda.html", context)

def buscar_pedido(request):
    criterio = request.GET.get("criterio")
    context = { "pedidos": Pedido.objects.filter(nombre_comprador__icontains=criterio)}
    return render(request, "AppAscenzi/busqueda.html", context)

def Mayorista_formulario(request):
    if request.method == 'POST':
        ped_form = MayForm(request.POST)
        ped_form.save()
    context = {
        "form": MayForm(),
        "mayoristas": Mayorista.objects.all()
    }
    return render(request,"AppAscenzi/mayorista.html", context)
   
def Minorista_formulario(request):
    if request.method == 'POST':
        ped_form = MinForm(request.POST)
        ped_form.save()
    context = {
        "form": MinForm(),
        "minoristas": Minorista.objects.all()
    }
    return render(request,"AppAscenzi/minorista.html", context)

def Pedidos_formulario(request):
    if request.method == 'POST':
        ped_form = PedForm(request.POST)
        ped_form.save()
    context = {
        "form": PedForm(),
        "pedidos": Pedido.objects.all()
    }
    return render(request,"AppAscenzi/pedidos.html", context)