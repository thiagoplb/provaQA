from math import isfinite


def calcular_desconto(valor_compra, tipo_cliente):
    if isinstance(valor_compra, bool) or not isinstance(valor_compra, (int, float)):
        raise TypeError("valor_compra deve ser int ou float")
    if isinstance(valor_compra, float) and not isfinite(valor_compra):
        raise ValueError("valor_compra deve ser finito")
    if valor_compra < 0:
        raise ValueError("valor_compra deve ser nao negativo")
    if not isinstance(tipo_cliente, str):
        raise TypeError("tipo_cliente deve ser texto")
    tipo_cliente = tipo_cliente.strip().upper()
    if tipo_cliente not in ("COMUM", "VIP"):
        raise ValueError("tipo_cliente deve ser COMUM ou VIP")

    desconto = 0

    if 100 <= valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20
    if tipo_cliente == "VIP":
        desconto += 0.05
    valor_desconto = valor_compra * desconto

    if valor_desconto > 200:
        valor_desconto = 200
    return round(valor_desconto, 2)
