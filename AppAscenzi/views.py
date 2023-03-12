from django.shortcuts import render

def index(request):
    return render(request, "AppAscenzi/index.html")

def pedidos(request):
    return render(request, "AppAscenzi/pedidos.html" )

def form_minor(request):
    return render(request, "AppAscenzi/minorista.html")

def form_mayor(request):
    return render(request, "AppAscenzi/mayorista.html")

def busqueda(request):
    return render(request, "AppAscenzi/busqueda.html")

def index(request):
    return render(request, "AppAscenzi/index.html")

def Venta_minorista(request):
    return render (request, "AppAscenzi/VentaMinorista.html")

def Venta_mayorista(request):
    return render (request, "AppAscenzi/VentaMayorista.html")

def Mayorista_formulario(request):
      if request.method == 'POST':
      
            nombre =  nombre(request.post['nombre'],(request.post['apellido']))
 
            nombre.save()
 
            return render(request, "AppAscenzi/index.html")
 
      return render(request,"AppAscenzi/VentaMayorista.html")

def Minorista_formulario(request):
      if request.method == 'POST':
      
            nombre =  nombre(request.post['nombre'],(request.post['apellido']))
 
            nombre.save()
 
            return render(request, "AppAscenzi/index.html")
 
      return render(request,"AppAscenzi/VentaMinorista.html")