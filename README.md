# Sistema de Gestão de Peças - Linha de Montagem

Sistema desenvolvido em Python para controle de qualidade e armazenamento de peças industriais.

## Como rodar

1. Certifique-se de ter o Python 3 instalado na sua máquina
2. Baixe o arquivo `sistema.py`
3. Abra o terminal na pasta onde salvou o arquivo
4. Execute o comando:

```bash
python3 sistema.py
```

## Funcionamento

O sistema exibe um menu com 5 opções:

- **Opção 1 - Cadastrar nova peça:** informa o ID, peso (gramas), comprimento (cm) e cor. O sistema avalia automaticamente se a peça é aprovada ou reprovada.
- **Opção 2 - Listar peças:** mostra todas as peças cadastradas separadas por aprovadas e reprovadas, com o motivo da reprovação.
- **Opção 3 - Remover peça:** remove uma peça pelo ID.
- **Opção 4 - Listar caixas:** mostra as caixas fechadas e a caixa que está em uso no momento.
- **Opção 5 - Relatório final:** exibe um resumo geral com totais e motivos de reprovação.

## Critérios de aprovação

| Critério    | Valor aceito      |
| ----------- | ----------------- |
| Peso        | Entre 95g e 105g  |
| Cor         | Azul ou Verde     |
| Comprimento | Entre 10cm e 20cm |

Peças aprovadas são armazenadas em caixas de até **10 peças**. Quando uma caixa enche, ela é fechada automaticamente e uma nova é aberta.

## Exemplos de uso

**Cadastrando uma peça aprovada:**

```
ID da peca: P001
Peso (em gramas): 100
Comprimento (em cm): 15
Cor da peca: azul

  APROVADA! Peca P001 adicionada na caixa 1.
```

**Cadastrando uma peça reprovada:**

```
ID da peca: P002
Peso (em gramas): 80
Comprimento (em cm): 25
Cor da peca: vermelho

  REPROVADA! Motivo(s):
    - peso fora do limite (deve ser entre 95g e 105g)
    - cor invalida (deve ser azul ou verde)
    - comprimento fora do limite (deve ser entre 10cm e 20cm)
```

**Relatório final:**

```
========== RELATORIO FINAL ==========
Total de pecas cadastradas : 5
Total de pecas aprovadas   : 3
Total de pecas reprovadas  : 2
Caixas utilizadas          : 1
  - Caixas fechadas        : 0
  - Caixa em aberto        : 1 (3 pecas)

Motivos de reprovacao:
  - peso fora do limite (deve ser entre 95g e 105g): 1 vez(es)
  - cor invalida (deve ser azul ou verde): 2 vez(es)
=====================================
```
