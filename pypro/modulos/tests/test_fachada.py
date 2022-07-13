import pytest
from model_mommy import mommy

from pypro.modulos import fachada
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [mommy.make(Modulo, titulo=s) for s in 'Antes Dpois'.split()]


def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key = lambda modulo: modulo.titulo)) == fachada.listar_modulos_ordenados()