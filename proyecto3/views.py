from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = "Bienvenido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def comprar(request):
    compra = "Comprar"
    pagina_html = HttpResponse(compra)
    print("Compra completada")
    return pagina_html
  
def devolver(request):
    devolucion = "Devolución"
    pagina_html = HttpResponse(devolucion)
    print("Devolución completada")
    return pagina_html
    