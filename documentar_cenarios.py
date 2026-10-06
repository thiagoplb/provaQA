"""Gera a tabela de cenarios a partir dos dados publicos da suite de testes."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
casos = runpy.run_path(str(root / "tests" / "test_desconto.py"))["CASOS"]
grupos = [
    (range(1, 3), "Compra de valor zero"),
    (range(3, 5), "Compra abaixo de R$ 100; VIP recebe 5%"),
    (range(5, 11), "Limite de R$ 100: imediatamente antes, no limite e depois"),
    (range(11, 13), "Compra intermediaria na faixa de 10%"),
    (range(13, 19), "Limite de R$ 500: imediatamente antes, no limite e depois"),
    (range(19, 24), "VIP com letras minusculas ou capitalizacao mista"),
    (range(24, 25), "Cliente comum sem adicional"),
    (range(25, 28), "Teto COMUM: antes, no limite e depois de R$ 1000"),
    (range(28, 31), "Teto VIP: antes, no limite e depois de R$ 800"),
    (range(31, 33), "Compra alta: desconto limitado a R$ 200"),
    (range(33, 35), "Arredondamento a duas casas decimais"),
    (range(35, 37), "Desconto abaixo do teto sem arredondar para R$ 200"),
]
linhas = ["# Cenarios de testes", "", "Todos os valores esperados representam o desconto em reais, nao o total da compra.", "", "| ID | Valor da compra (R$) | Tipo de cliente | Desconto esperado (R$) | Objetivo |", "| --- | ---: | --- | ---: | --- |"]
for identificador, compra, cliente, esperado in casos:
    numero = int(identificador[1:])
    objetivo = next(texto for intervalo, texto in grupos if numero in intervalo)
    linhas.append(f"| {identificador} | {compra:.2f} | `{cliente}` | {esperado:.2f} | {objetivo} |")
linhas += ["", "## Falhas encontradas no codigo original", "", "| Cenario | Esperado (R$) | Recebido (R$) | Causa |", "| --- | ---: | ---: | --- |", "| C07 | 10.00 | 0.00 | Limite de R$ 100 excluido |", "| C08 | 15.00 | 5.00 | Limite de R$ 100 excluido |", "| C19 | 2.50 | 0.00 | VIP minusculo nao reconhecido |", "| C20 | 45.00 | 30.00 | VIP minusculo nao reconhecido |", "| C21 | 125.00 | 100.00 | VIP minusculo nao reconhecido |", "| C22 | 45.00 | 30.00 | Capitalizacao mista nao reconhecida |", "| C23 | 45.00 | 30.00 | Capitalizacao mista nao reconhecida |", "", "Apos corrigir os dois bugs, os mesmos 36 cenarios passaram.", "", "Valores de R$ 999,99 (COMUM) e R$ 799,99 (VIP) arredondam para R$ 200,00. C35 e C36 verificam resultados realmente inferiores ao teto.", "", "Entradas invalidas nao possuem criterios de aceite definidos nesta historia e nao fazem parte desta suite.", ""]
(root / "CENARIOS.md").write_text("\n".join(linhas), encoding="utf-8")
