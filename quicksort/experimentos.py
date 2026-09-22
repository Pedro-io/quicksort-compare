"""Execução dos experimentos com medição de tempo e contadores.

O tempo de execução é medido com a função time.perf_counter, que utiliza o
relógio de maior precisão disponível na máquina, conforme exigido pelo
enunciado do trabalho.
"""

import sys
import time


def ajustar_limite_de_recursao(profundidade_maxima):
    """Ajusta o limite de recursão do interpretador, se necessário.

    O Quicksort clássico atinge profundidade de recursão proporcional ao
    tamanho do vetor em seu pior caso, portanto o limite padrão do
    interpretador pode ser insuficiente para os experimentos.
    """
    limite = max(sys.getrecursionlimit(), profundidade_maxima + 1000)
    sys.setrecursionlimit(limite)


def medir_execucao(ordenador, dados, repeticoes=5):
    """Executa o ordenador várias vezes sobre cópias idênticas dos dados.

    Retorna um dicionário com o tempo médio, o número médio de comparações e
    o número médio de trocas, além das listas com os valores individuais de
    cada repetição.
    """
    tempos = []
    comparacoes = []
    trocas = []
    for _ in range(repeticoes):
        copia = dados[:]
        inicio = time.perf_counter()
        ordenador.ordenar(copia)
        fim = time.perf_counter()
        tempos.append(fim - inicio)
        comparacoes.append(ordenador.comparacoes)
        trocas.append(ordenador.trocas)
    return {
        "tempo_medio": sum(tempos) / repeticoes,
        "comparacoes_media": sum(comparacoes) / repeticoes,
        "trocas_media": sum(trocas) / repeticoes,
        "tempos": tempos,
        "comparacoes": comparacoes,
        "trocas": trocas,
    }


def executar_comparativo(versoes, massas, repeticoes=5):
    """Executa todas as versões sobre todas as massas de teste.

    versoes: lista de instâncias de ordenadores;
    massas: dicionário com o nome da massa e o vetor de dados.
    """
    resultados = {}
    for nome_massa, dados in massas.items():
        resultados[nome_massa] = {}
        for ordenador in versoes:
            resultados[nome_massa][ordenador.nome] = medir_execucao(
                ordenador, dados, repeticoes
            )
    return resultados


def verificar_ordenacao(ordenador, dados):
    """Verifica se o ordenador produz o mesmo resultado que a função sorted."""
    copia = dados[:]
    ordenador.ordenar(copia)
    return copia == sorted(dados)
