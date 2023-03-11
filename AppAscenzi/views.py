from django.shortcuts import render

def index(request):
    return render(request, "AppAscenzi/index.html")

def mostrar_mi_template(request):
    return render (request, "AppAscenzi/index.html")