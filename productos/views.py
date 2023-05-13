from django.shortcuts import render

def listar_productos(request):
    contexto = {
        "productos": [
            {"nombre":"jarra de agua", "modelo":"amazon basics"},
            {"nombre":"pava electrica", "modelo":"cecotec"},
            {"nombre":"tv smart", "modelo":"samsungPro"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='productos/lista_productos.html',
        contexto=contexto,
    )
    return http_responde


def listar_clientes(request):
    contexto = {
        "clientes": [
            {"nombre":"Antonella", "modelo":"Sardi"},
            {"nombre":"David", "modelo":"Escudero"},
            {"nombre":"Gisela", "modelo":"Merlinez"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='productos/listar_clientes.html',
        contexto=contexto,
    )
    return http_responde
# Create your views here.

