from django.contrib import admin
from django.urls import path
from AppAscenzi.views import (index, pedidos, buscar_minorista, buscar_mayorista, buscar_pedido, Mayorista_formulario, Minorista_formulario, Pedidos_formulario,
    MinList, MinDetail, MinUpdate, MinDelete, MinCreate, MinSearch
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('mis-pedidos', pedidos, name="pedidos"),
    path('buscar-minorista', buscar_minorista, name="buscar_minorista"),
    path('buscar-mayorista', buscar_mayorista, name="buscar_mayorista"),
    path('buscar-pedido', buscar_pedido, name="buscar_pedidos"),
    path('formulario-mayorista/', Mayorista_formulario, name="mayorista_formulario"),
    path('formulario-minorista/', Minorista_formulario, name="minorista_formulario"),
    path('formulario-pedido/', Pedidos_formulario, name="pedidos_formulario"),
    path('minorista/list', MinList.as_view(), name="min-list"),
    path('minorista/<pk>/detail', MinDetail.as_view(), name="min-detail"),
    path('minorista/<pk>/update', MinUpdate.as_view(), name="min-update"),
    path('minorista/<pk>/delete', MinDelete.as_view(), name="min-delete"),
    path('minorista/create', MinCreate.as_view(), name="min-create"),
    path('minorista/search', MinSearch.as_view(), name="min-search"),
]
