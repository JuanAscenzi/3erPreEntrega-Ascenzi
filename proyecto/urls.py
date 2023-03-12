"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppAscenzi.views import index, pedidos, form_minor, form_mayor, busqueda, Venta_mayorista, Venta_minorista, Minorista_formulario, Mayorista_formulario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('mis-pedidos/', pedidos, name="pedidos"),
    path('compra-minorista/', form_minor, name="minorista"),
    path('compra-mayorista/', form_mayor, name="mayorista"),
    path('buscar/', busqueda, name="busqueda"),
    path('venta-minorista/', Venta_minorista, name="minorista"),
    path('venta-mayorista/', Venta_mayorista, name="mayorista"),
    path('formulario-mayorista/', Mayorista_formulario, name="mayorista_formulario"),
    path('formulario-minorista/', Minorista_formulario, name="minorista_formulario"),
]

