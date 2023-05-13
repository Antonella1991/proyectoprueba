from django.contrib import admin
from django.urls import path

from productos.views import listar_productos, listar_clientes

path('listado-productos/', listar_productos),
path('listado-clientes/', listar_clientes),