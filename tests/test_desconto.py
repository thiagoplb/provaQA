import pytest


# Resultados esperados fixos, definidos pelos criterios de aceite da historia.
CASOS = [
    ("C01", 0, "COMUM", 0),
    ("C02", 50, "VIP", 2.50),
    ("C03", 99.99, "COMUM", 0),
    ("C04", 99.99, "VIP", 5.00),
    ("C05", 100, "COMUM", 10.00),
    ("C06", 100, "VIP", 15.00),
    ("C07", 300, "COMUM", 30.00),
    ("C08", 300, "VIP", 45.00),
    ("C09", 499.99, "COMUM", 50.00),
    ("C10", 499.99, "VIP", 75.00),
    ("C11", 500, "COMUM", 100.00),
    ("C12", 500, "VIP", 125.00),
    ("C13", 300, "vip", 45.00),
    ("C14", 300, "Vip", 45.00),
    ("C15", 1000, "COMUM", 200.00),
    ("C16", 800, "VIP", 200.00),
    ("C17", 5000, "COMUM", 200.00),
    ("C18", 5000, "VIP", 200.00),
    ("C19", 123.45, "COMUM", 12.35),
    ("C20", 123.45, "VIP", 18.52),
    ("C21", 999, "COMUM", 199.80),
    ("C22", 799, "VIP", 199.75),
    ("C23", 300, " VIP ", 45.00),
    ("C24", 300, " COMUM ", 30.00),
]


@pytest.mark.parametrize("cenario,valor_compra,tipo_cliente,esperado", CASOS, ids=[caso[0] for caso in CASOS])
def test_criterios_de_aceite(calcular_desconto, cenario, valor_compra, tipo_cliente, esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)
    assert resultado == esperado, f"{cenario}: esperado {esperado:.2f}, recebido {resultado:.2f}"
    assert 0 <= resultado <= 200


# Validacoes adicionais adotadas para dados inesperados.
CASOS_INVALIDOS = [
    ("I01", -0.01, "COMUM", ValueError, "valor_compra deve ser int ou float nao negativo"),
    ("I02", "", "COMUM", TypeError, "valor_compra deve ser int ou float nao negativo"),
    ("I03", "300", "COMUM", TypeError, "valor_compra deve ser int ou float nao negativo"),
    ("I04", "abc", "COMUM", TypeError, "valor_compra deve ser int ou float nao negativo"),
    ("I05", 300, "123", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I06", 300, "", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I07", 300, "   ", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I08", 300, "PREMIUM", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
]


@pytest.mark.parametrize(
    "cenario,valor_compra,tipo_cliente,erro,mensagem",
    CASOS_INVALIDOS,
    ids=[caso[0] for caso in CASOS_INVALIDOS],
)
def test_dados_inesperados(calcular_desconto, cenario, valor_compra, tipo_cliente, erro, mensagem):
    with pytest.raises(erro, match=mensagem):
        calcular_desconto(valor_compra, tipo_cliente)
