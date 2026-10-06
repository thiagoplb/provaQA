import pytest


# Resultados esperados fixos, definidos pelos criterios de aceite da historia.
CASOS = [
    ("C01", 0, "COMUM", 0),
    ("C02", 0, "VIP", 0),
    ("C03", 50, "COMUM", 0),
    ("C04", 50, "VIP", 2.50),
    ("C05", 99.99, "COMUM", 0),
    ("C06", 99.99, "VIP", 5.00),
    ("C07", 100, "COMUM", 10.00),
    ("C08", 100, "VIP", 15.00),
    ("C09", 100.01, "COMUM", 10.00),
    ("C10", 100.01, "VIP", 15.00),
    ("C11", 300, "COMUM", 30.00),
    ("C12", 300, "VIP", 45.00),
    ("C13", 499.99, "COMUM", 50.00),
    ("C14", 499.99, "VIP", 75.00),
    ("C15", 500, "COMUM", 100.00),
    ("C16", 500, "VIP", 125.00),
    ("C17", 500.01, "COMUM", 100.00),
    ("C18", 500.01, "VIP", 125.00),
    ("C19", 50, "vip", 2.50),
    ("C20", 300, "vip", 45.00),
    ("C21", 500, "vip", 125.00),
    ("C22", 300, "Vip", 45.00),
    ("C23", 300, "vIp", 45.00),
    ("C24", 300, "comum", 30.00),
    ("C25", 999.99, "COMUM", 200.00),
    ("C26", 1000, "COMUM", 200.00),
    ("C27", 1000.01, "COMUM", 200.00),
    ("C28", 799.99, "VIP", 200.00),
    ("C29", 800, "VIP", 200.00),
    ("C30", 800.01, "VIP", 200.00),
    ("C31", 5000, "COMUM", 200.00),
    ("C32", 5000, "VIP", 200.00),
    ("C33", 123.45, "COMUM", 12.35),
    ("C34", 123.45, "VIP", 18.52),
    ("C35", 999, "COMUM", 199.80),
    ("C36", 799, "VIP", 199.75),
    ("C37", 300, " VIP ", 45.00),
    ("C38", 50, " vip ", 2.50),
    ("C39", 300, " COMUM ", 30.00),
    ("C40", 500, "CoMuM", 100.00),
]


@pytest.mark.parametrize("cenario,valor_compra,tipo_cliente,esperado", CASOS, ids=[caso[0] for caso in CASOS])
def test_criterios_de_aceite(calcular_desconto, cenario, valor_compra, tipo_cliente, esperado):
    resultado = calcular_desconto(valor_compra, tipo_cliente)
    assert resultado == esperado, f"{cenario}: esperado {esperado:.2f}, recebido {resultado:.2f}"
    assert 0 <= resultado <= 200


# Validacoes adicionais adotadas para dados inesperados.
CASOS_INVALIDOS = [
    ("I01", -0.01, "COMUM", ValueError, "valor_compra deve ser nao negativo"),
    ("I02", -100, "VIP", ValueError, "valor_compra deve ser nao negativo"),
    ("I03", "", "COMUM", TypeError, "valor_compra deve ser int ou float"),
    ("I04", "300", "COMUM", TypeError, "valor_compra deve ser int ou float"),
    ("I05", "abc", "COMUM", TypeError, "valor_compra deve ser int ou float"),
    ("I06", "   ", "VIP", TypeError, "valor_compra deve ser int ou float"),
    ("I07", 300, "123", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I08", 300, "", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I09", 300, "   ", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
    ("I10", 300, "PREMIUM", ValueError, "tipo_cliente deve ser COMUM ou VIP"),
]


@pytest.mark.parametrize(
    "cenario,valor_compra,tipo_cliente,erro,mensagem",
    CASOS_INVALIDOS,
    ids=[caso[0] for caso in CASOS_INVALIDOS],
)
def test_dados_inesperados(calcular_desconto, cenario, valor_compra, tipo_cliente, erro, mensagem):
    with pytest.raises(erro, match=mensagem):
        calcular_desconto(valor_compra, tipo_cliente)
