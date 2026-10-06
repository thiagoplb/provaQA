import importlib
import pytest

# A mesma suite deve rodar nas versoes original e corrigida.


def pytest_addoption(parser):
    parser.addoption("--implementacao", choices=("corrigida", "original"), default="corrigida")


@pytest.fixture
def calcular_desconto(request):
    nome = "desconto_original" if request.config.getoption("--implementacao") == "original" else "desconto"
    return importlib.import_module(nome).calcular_desconto
