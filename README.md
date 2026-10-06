# Auditoria de descontos — Tech UniDiasUp

Projeto Python/Pytest que verifica os cinco criterios de aceite da historia de usuario.
A funcao retorna o desconto em reais, e nao o total da compra apos desconto.

## Resultado da auditoria

- Codigo original: **7 falhas e 29 sucessos**.
- Codigo corrigido: **36 sucessos**.
- Bug 1: `valor_compra > 100` excluia o limite de R$ 100. Corrigido para `100 <= valor_compra < 500`.
- Bug 2: a comparacao literal com `VIP` ignorava `vip`, `Vip` e `vIp`. Corrigido com `tipo_cliente.upper()`.
- A faixa de 20%, o adicional de 5 pontos percentuais e o teto de R$ 200 ja estavam corretos.

Veja a tabela completa em [CENARIOS.md](CENARIOS.md).

Antes da correcao:

![PRINT1 — 7 falhas e 29 sucessos](evidencias/PRINT1.png)

Depois da correcao:

![PRINT2 — 36 sucessos](evidencias/PRINT2.png)

## Arquivos

- `desconto.py`: funcao corrigida.
- `desconto_original.py`: logica original preservada para reproduzir as falhas.
- `tests/test_desconto.py`: 36 cenarios com resultados esperados fixos.
- `CENARIOS.md`: entradas e resultados esperados de todos os cenarios.
- `evidencias/PRINT1.png`: captura no navegador do log real da execucao original.
- `evidencias/PRINT2.png`: captura no navegador do log real da execucao corrigida.
- `evidencias/PRINT1.txt` e `PRINT2.txt`: saidas completas do Pytest.
- `evidencias/execucoes.json`: comandos, codigos de saida e hashes dos logs.

Os PNGs sao capturas das paginas HTML que exibem as saidas reais salvas pelo Pytest; nao sao fotografias de uma janela de terminal.

## Executar

```powershell
python -m pip install -r requirements.txt
python -m pytest -p no:cacheprovider -v
python -m pytest -p no:cacheprovider -v --implementacao original
```

A execucao original deve falhar: os mesmos testes e os mesmos valores esperados sao usados nas duas versoes.
O cache do Pytest e desativado nesses comandos para evitar arquivos temporarios; isso nao altera os testes.

Para regenerar os logs e os prints no Windows com Microsoft Edge instalado:

```powershell
python registrar_evidencias.py
```

## Escopo

Cobertura: valores zero e abaixo de R$ 100, limites imediatamente antes/no/depois de R$ 100 e R$ 500, clientes comuns e VIP, variacoes de capitalizacao, teto antes/no/depois dos limites de compra de R$ 800 (VIP) e R$ 1000 (COMUM), compras altas e arredondamento a duas casas.
Os valores de R$ 799 e R$ 999 distinguem descontos abaixo do teto dos valores que arredondam para R$ 200.
Entradas negativas, tipos invalidos, categorias desconhecidas, espacos e criterios especiais de arredondamento nao foram definidos pelo PO; os testes nao inventam regras para esses casos.
Foi preservado o arredondamento com `round(valor_desconto, 2)` do codigo original.

## Publicacao no GitHub

O projeto foi preparado como repositorio Git local. A publicacao exige a URL do repositorio de destino e autenticacao com permissao de escrita. Depois de definir esse destino, use:

```powershell
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

## Texto para a entrega

Foram elaborados 36 testes unitarios automatizados usando Pytest, cobrindo as faixas de desconto, valores limite, adicional VIP sem diferenciar maiusculas e minusculas, teto de R$ 200 e arredondamento. A primeira execucao apresentou 7 falhas e 29 sucessos. Foram identificados dois bugs: exclusao de compras de exatamente R$ 100 da faixa de 10% e reconhecimento de VIP somente em maiusculas. Depois das correcoes, os mesmos 36 testes passaram. As evidencias anteriores e posteriores estao em PRINT1 e PRINT2.
