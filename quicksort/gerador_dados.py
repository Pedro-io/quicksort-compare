"""Geração das massas de teste utilizadas nos experimentos.

As massas disponíveis são:

    - aleatorio: valores sorteados uniformemente em um intervalo amplo;
    - ordenado: valores já em ordem crescente;
    - inverso: valores em ordem decrescente;
    - repetidos: valores sorteados em um intervalo pequeno, o que produz
      muitos elementos repetidos.

Quando uma semente é informada, a geração é determinística, garantindo que
todas as versões e todas as repetições utilizem exatamente as mesmas massas
de dados.
"""

import random


def vetor_aleatorio(tamanho, semente=None):
    """Retorna um vetor com elementos aleatórios entre 0 e 999999."""
    gerador = random.Random(semente)
    return [gerador.randint(0, 999999) for _ in range(tamanho)]


def vetor_ordenado(tamanho, semente=None):
    """Retorna um vetor com os valores de 0 a tamanho - 1, já ordenado."""
    return list(range(tamanho))


def vetor_ordenado_inversamente(tamanho, semente=None):
    """Retorna um vetor com os valores em ordem decrescente."""
    return list(range(tamanho, 0, -1))


def vetor_com_muitos_repetidos(tamanho, semente=None):
    """Retorna um vetor com muitos elementos repetidos.

    Os valores são sorteados no intervalo de 0 a 99, o que garante alta
    frequência de repetições.
    """
    gerador = random.Random(semente)
    return [gerador.randint(0, 99) for _ in range(tamanho)]


def gerar_massa(nome, tamanho, semente=None):
    """Gera uma massa de teste conforme o nome informado."""
    if nome == "aleatorio":
        return vetor_aleatorio(tamanho, semente)
    if nome == "ordenado":
        return vetor_ordenado(tamanho)
    if nome == "inverso":
        return vetor_ordenado_inversamente(tamanho)
    if nome == "repetidos":
        return vetor_com_muitos_repetidos(tamanho, semente)
    raise ValueError("Massa de teste desconhecida: {}".format(nome))
