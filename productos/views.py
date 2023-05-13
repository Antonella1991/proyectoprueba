from django.shortcuts import render

def listar_estudiantes(request):
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
# Create your views here.

