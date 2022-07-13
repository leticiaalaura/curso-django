from pypro.modulos import fachada


def listar_modulos(request):
    return {'MODULOS': fachada.listar_modulos_ordenados()}