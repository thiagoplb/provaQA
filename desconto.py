def calcular_desconto(valor_compra, tipo_cliente):
    """Retorna o desconto em reais, com adicional VIP e teto de R$ 200."""
    desconto = 0

    # Desconto base: 0%, 10% ou 20%.
    if 100 <= valor_compra < 500:
        desconto = 0.10
    elif valor_compra >= 500:
        desconto = 0.20
    # VIP recebe mais 5 pontos percentuais em qualquer faixa.
    if tipo_cliente.upper() == "VIP":
        desconto += 0.05
    valor_desconto = valor_compra * desconto

    # O teto se aplica ao valor do desconto, depois do adicional VIP.
    if valor_desconto > 200:
        valor_desconto = 200
    return round(valor_desconto, 2)
