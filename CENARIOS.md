# Cenarios de testes

Todos os valores esperados representam o desconto em reais, nao o total da compra.

| ID | Valor da compra (R$) | Tipo de cliente | Desconto esperado (R$) | Objetivo |
| --- | ---: | --- | ---: | --- |
| C01 | 0.00 | `COMUM` | 0.00 | Compra de valor zero |
| C02 | 0.00 | `VIP` | 0.00 | Compra de valor zero |
| C03 | 50.00 | `COMUM` | 0.00 | Compra abaixo de R$ 100; VIP recebe 5% |
| C04 | 50.00 | `VIP` | 2.50 | Compra abaixo de R$ 100; VIP recebe 5% |
| C05 | 99.99 | `COMUM` | 0.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C06 | 99.99 | `VIP` | 5.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C07 | 100.00 | `COMUM` | 10.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C08 | 100.00 | `VIP` | 15.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C09 | 100.01 | `COMUM` | 10.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C10 | 100.01 | `VIP` | 15.00 | Limite de R$ 100: imediatamente antes, no limite e depois |
| C11 | 300.00 | `COMUM` | 30.00 | Compra intermediaria na faixa de 10% |
| C12 | 300.00 | `VIP` | 45.00 | Compra intermediaria na faixa de 10% |
| C13 | 499.99 | `COMUM` | 50.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C14 | 499.99 | `VIP` | 75.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C15 | 500.00 | `COMUM` | 100.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C16 | 500.00 | `VIP` | 125.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C17 | 500.01 | `COMUM` | 100.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C18 | 500.01 | `VIP` | 125.00 | Limite de R$ 500: imediatamente antes, no limite e depois |
| C19 | 50.00 | `vip` | 2.50 | VIP com letras minusculas ou capitalizacao mista |
| C20 | 300.00 | `vip` | 45.00 | VIP com letras minusculas ou capitalizacao mista |
| C21 | 500.00 | `vip` | 125.00 | VIP com letras minusculas ou capitalizacao mista |
| C22 | 300.00 | `Vip` | 45.00 | VIP com letras minusculas ou capitalizacao mista |
| C23 | 300.00 | `vIp` | 45.00 | VIP com letras minusculas ou capitalizacao mista |
| C24 | 300.00 | `comum` | 30.00 | Cliente comum sem adicional |
| C25 | 999.99 | `COMUM` | 200.00 | Teto COMUM: antes, no limite e depois de R$ 1000 |
| C26 | 1000.00 | `COMUM` | 200.00 | Teto COMUM: antes, no limite e depois de R$ 1000 |
| C27 | 1000.01 | `COMUM` | 200.00 | Teto COMUM: antes, no limite e depois de R$ 1000 |
| C28 | 799.99 | `VIP` | 200.00 | Teto VIP: antes, no limite e depois de R$ 800 |
| C29 | 800.00 | `VIP` | 200.00 | Teto VIP: antes, no limite e depois de R$ 800 |
| C30 | 800.01 | `VIP` | 200.00 | Teto VIP: antes, no limite e depois de R$ 800 |
| C31 | 5000.00 | `COMUM` | 200.00 | Compra alta: desconto limitado a R$ 200 |
| C32 | 5000.00 | `VIP` | 200.00 | Compra alta: desconto limitado a R$ 200 |
| C33 | 123.45 | `COMUM` | 12.35 | Arredondamento a duas casas decimais |
| C34 | 123.45 | `VIP` | 18.52 | Arredondamento a duas casas decimais |
| C35 | 999.00 | `COMUM` | 199.80 | Desconto abaixo do teto sem arredondar para R$ 200 |
| C36 | 799.00 | `VIP` | 199.75 | Desconto abaixo do teto sem arredondar para R$ 200 |

## Falhas encontradas no codigo original

| Cenario | Esperado (R$) | Recebido (R$) | Causa |
| --- | ---: | ---: | --- |
| C07 | 10.00 | 0.00 | Limite de R$ 100 excluido |
| C08 | 15.00 | 5.00 | Limite de R$ 100 excluido |
| C19 | 2.50 | 0.00 | VIP minusculo nao reconhecido |
| C20 | 45.00 | 30.00 | VIP minusculo nao reconhecido |
| C21 | 125.00 | 100.00 | VIP minusculo nao reconhecido |
| C22 | 45.00 | 30.00 | Capitalizacao mista nao reconhecida |
| C23 | 45.00 | 30.00 | Capitalizacao mista nao reconhecida |

Apos corrigir os dois bugs, os mesmos 36 cenarios passaram.

Valores de R$ 999,99 (COMUM) e R$ 799,99 (VIP) arredondam para R$ 200,00. C35 e C36 verificam resultados realmente inferiores ao teto.

Entradas invalidas nao possuem criterios de aceite definidos nesta historia e nao fazem parte desta suite.
