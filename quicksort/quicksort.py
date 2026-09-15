"""Implementações do algoritmo Quicksort para o Trabalho Prático de PAA.

Este módulo contém três versões do Quicksort:

    1. Quicksort recursivo clássico, com pivô no último elemento;
    2. Quicksort híbrido, com ordenação por inserção para subvetores com
       menos de M elementos;
    3. Quicksort híbrido com escolha do pivô pela mediana de três.

Todas as versões mantêm contadores de comparações e de trocas, atualizados
durante a execução, e ordenam o vetor in-place, conforme exigido pelo
enunciado do trabalho.

Convenções adotadas:

    - Uma comparação é contabilizada a cada comparação entre dois elementos
      (ou entre um elemento e a chave ou o pivô).
    - Uma troca é contabilizada a cada troca de posição entre dois elementos.
    - Na ordenação por inserção, cada deslocamento de um elemento para a
      direita é contabilizado como uma troca. A escrita da chave em sua
      posição final não é contabilizada, pois não caracteriza uma troca entre
      duas posições.
    - Na escolha do pivô pela mediana de três, as três comparações realizadas
      e as eventuais trocas entre os três elementos são contabilizadas, assim
      como a movimentação do pivô para o último elemento antes da partição.
"""


class OrdenadorBase:
    """Classe base que mantém os contadores de comparações e de trocas."""

    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0
        self.nome = "Quicksort"

    def reiniciar_contadores(self):
        """Zera os contadores de comparações e de trocas."""
        self.comparacoes = 0
        self.trocas = 0

    def ordenar(self, vetor):
        """Ordena o vetor in-place e retorna a referência para o vetor.

        Os contadores de comparações e de trocas são zerados no início da
        execução e acumulam os valores da última ordenação realizada.
        """
        self.reiniciar_contadores()
        if len(vetor) > 1:
            self._ordenar_intervalo(vetor, 0, len(vetor) - 1)
        return vetor

    def _trocar(self, vetor, i, j):
        """Troca dois elementos de posição, contabilizando a operação."""
        if i != j:
            vetor[i], vetor[j] = vetor[j], vetor[i]
            self.trocas += 1

    def _particionar(self, vetor, inicio, fim):
        """Particionamento de Lomuto, com o pivô no último elemento.

        Retorna a posição final do pivô após a partição.
        """
        pivo = vetor[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            self.comparacoes += 1
            if vetor[j] <= pivo:
                i += 1
                self._trocar(vetor, i, j)
        self._trocar(vetor, i + 1, fim)
        return i + 1

    def _insercao(self, vetor, inicio, fim):
        """Ordenação por inserção aplicada a um intervalo do vetor."""
        for i in range(inicio + 1, fim + 1):
            chave = vetor[i]
            j = i - 1
            while j >= inicio and vetor[j] > chave:
                self.comparacoes += 1
                vetor[j + 1] = vetor[j]
                self.trocas += 1
                j -= 1
            if j >= inicio:
                self.comparacoes += 1
            vetor[j + 1] = chave

    def _ordenar_intervalo(self, vetor, inicio, fim):
        raise NotImplementedError


class QuicksortRecursivo(OrdenadorBase):
    """Quicksort recursivo clássico.

    O pivô é sempre o último elemento do intervalo. Essa escolha faz com que
    vetores já ordenados caracterizem o pior caso do algoritmo, pois as
    partições ficam completamente desbalanceadas.
    """

    def __init__(self):
        super().__init__()
        self.nome = "Quicksort recursivo"

    def _ordenar_intervalo(self, vetor, inicio, fim):
        if inicio < fim:
            posicao_pivo = self._particionar(vetor, inicio, fim)
            self._ordenar_intervalo(vetor, inicio, posicao_pivo - 1)
            self._ordenar_intervalo(vetor, posicao_pivo + 1, fim)


class QuicksortHibrido(OrdenadorBase):
    """Quicksort híbrido com ordenação por inserção.

    A recursão é interrompida para subvetores com menos de M elementos, que
    são ordenados com o algoritmo de ordenação por inserção. O valor de M é
    determinado empiricamente em experimento próprio.
    """

    def __init__(self, m=10):
        super().__init__()
        self.m = m
        self.nome = "Quicksort híbrido (M = {})".format(m)

    def _ordenar_intervalo(self, vetor, inicio, fim):
        tamanho = fim - inicio + 1
        if tamanho < self.m:
            self._insercao(vetor, inicio, fim)
        elif inicio < fim:
            posicao_pivo = self._particionar(vetor, inicio, fim)
            self._ordenar_intervalo(vetor, inicio, posicao_pivo - 1)
            self._ordenar_intervalo(vetor, posicao_pivo + 1, fim)


class QuicksortHibridoMedianaTres(OrdenadorBase):
    """Quicksort híbrido com pivô pela mediana de três.

    O pivô é escolhido como a mediana entre o primeiro, o central e o último
    elemento do intervalo, o que reduz a probabilidade de partições
    desbalanceadas. O pivô é movido para o último elemento antes do
    particionamento de Lomuto.
    """

    def __init__(self, m=10):
        super().__init__()
        self.m = m
        self.nome = "Quicksort híbrido com mediana de três (M = {})".format(m)

    def _ordenar_intervalo(self, vetor, inicio, fim):
        tamanho = fim - inicio + 1
        if tamanho < self.m:
            self._insercao(vetor, inicio, fim)
        elif inicio < fim:
            posicao_pivo = self._mediana_de_tres(vetor, inicio, fim)
            self._trocar(vetor, posicao_pivo, fim)
            posicao_pivo = self._particionar(vetor, inicio, fim)
            self._ordenar_intervalo(vetor, inicio, posicao_pivo - 1)
            self._ordenar_intervalo(vetor, posicao_pivo + 1, fim)

    def _mediana_de_tres(self, vetor, inicio, fim):
        """Ordena os três elementos e retorna a posição da mediana.

        São realizadas três comparações e, no máximo, três trocas. Ao final, o
        menor elemento está em início, o maior em fim e a mediana em meio.
        """
        meio = (inicio + fim) // 2
        self.comparacoes += 1
        if vetor[inicio] > vetor[meio]:
            self._trocar(vetor, inicio, meio)
        self.comparacoes += 1
        if vetor[meio] > vetor[fim]:
            self._trocar(vetor, meio, fim)
        self.comparacoes += 1
        if vetor[inicio] > vetor[meio]:
            self._trocar(vetor, inicio, meio)
        return meio
