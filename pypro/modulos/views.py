from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from pypro.modulos import fachada


def indice(request):
    ctx = {'modulos': fachada.listar_modulos_com_aulas()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = fachada.encontrar_modulo(slug)
    aulas = fachada.listar_aulas_de_modulo_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


@login_required
def aula(request, slug):
    aula = fachada.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
