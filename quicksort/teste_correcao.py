"""Testes de correção das três versões do Quicksort.

Cada versão é executada sobre as quatro massas de teste, em diversos
tamanhos, e o resultado é comparado com a ordenação produzida pela função
embutida sorted do Python.
"""

from quicksort.experimentos import ajustar_limite_de_recursao
from quicksort.gerador_dados import gerar_massa
from quicksort.quicksort import (
    QuicksortHibrido,
    QuicksortHibridoMedianaTres,
    QuicksortRecursivo,
)


def testar():
    """Executa todos os testes e retorna o número de falhas encontradas."""
    # O pior caso do Quicksort clássico exige profundidade de recursão
    # proporcional ao tamanho do vetor.
    ajustar_limite_de_recursao(30000)
    geradores = ["aleatorio", "ordenado", "inverso", "repetidos"]
    versoes = [
        QuicksortRecursivo(),
        QuicksortHibrido(m=10),
        QuicksortHibridoMedianaTres(m=10),
    ]
    falhas = 0
    for tamanho in (0, 1, 2, 3, 10, 100, 1000, 5000):
        for nome_massa in geradores:
            dados = gerar_massa(nome_massa, tamanho, semente=42)
            esperado = sorted(dados)
            for versao in versoes:
                copia = dados[:]
                versao.ordenar(copia)
                if copia != esperado:
                    falhas += 1
                    print("Falha: {} | massa {} | tamanho {}".format(
                        versao.nome, nome_massa, tamanho
                    ))
    if falhas == 0:
        print("Todos os testes de correção passaram.")
    return falhas


if __name__ == "__main__":
    import sys

    sys.exit(1 if testar() else 0)
