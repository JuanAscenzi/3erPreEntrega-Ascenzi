from django.contrib import admin
from django.urls import path
from AppAscenzi.views import index, pedidos, busqueda, buscar_minorista, buscar_mayorista, buscar_pedido, Mayorista_formulario, Minorista_formulario, Pedidos_formulario, reset_Mayorista, reset_Minorista, reset_Pedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('mis-pedidos', pedidos, name="pedidos"),
    path('buscar', busqueda, name="busqueda"),
    path('buscar-minorista', buscar_minorista, name="buscar_minorista"),
    path('buscar-mayorista', buscar_mayorista, name="buscar_mayorista"),
    path('buscar-pedido', buscar_pedido, name="buscar_pedidos"),
    path('formulario-mayorista/', Mayorista_formulario, name="mayorista_formulario"),
    path('formulario-minorista/', Minorista_formulario, name="minorista_formulario"),
    path('formulario-pedido/', Pedidos_formulario, name="pedidos_formulario"),
    path('formulario-mayorista/reseteo', reset_Mayorista, name="mayorista_formulario_reseteado"),
    path('formulario-minorista/reseteo', reset_Minorista, name="minorista_formulario_reseteado"),
    path('formulario-pedido/reseteo', reset_Pedido, name="pedido_formulario_reseteado"),
]