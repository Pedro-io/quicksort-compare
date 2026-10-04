# Estudo Comparativo de Implementações do Quicksort

Trabalho Prático 1 da disciplina Projeto e Análise de Algoritmos (PAA), da Pontifícia Universidade Católica de Minas Gerais (PUC Minas), sob orientação do professor Walisson Ferreira de Carvalho.

O trabalho implementa e compara três versões do algoritmo Quicksort:

1. **Quicksort recursivo clássico**, com particionamento de Lomuto e pivô no último elemento;
2. **Quicksort híbrido**, em que a recursão é interrompida para subvetores com menos de M elementos, ordenados com o algoritmo de ordenação por inserção, sendo M determinado empiricamente;
3. **Quicksort híbrido com mediana de três**, em que o pivô é escolhido como a mediana entre o primeiro, o central e o último elemento do intervalo.

Todas as versões mantêm contadores de comparações e de trocas, utilizam o relógio da máquina para medir o tempo de execução e são executadas sobre massas de teste variadas (aleatória, ordenada, ordenada inversamente e com muitos elementos repetidos), com múltiplas repetições para obtenção de médias confiáveis. Um experimento específico força explicitamente o pior caso do Quicksort.

## Estrutura do repositório

- `quicksort/`: módulos Python com as implementações, a geração das massas de teste, os experimentos e os testes de correção;
- `notebooks/analise_quicksort.ipynb`: notebook com todas as análises, executável de ponta a ponta;
- `resultados/tabelas/`: tabelas em formato CSV com os resultados dos experimentos;
- `resultados/figuras/`: figuras geradas pelo notebook;
- `relatorio/`: versão em PDF do relatório final e as figuras utilizadas nele.

## Como executar

### 1. Ambiente virtual e dependências

Em um terminal na raiz do repositório:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

No Windows, o executável do ambiente fica em `.venv/Scripts/`, em Linux e macOS, em `.venv/bin/`.

### 2. Testes de correção

```bash
.venv/Scripts/python -m quicksort.teste_correcao
```

### 3. Notebook de análises

Para abrir o notebook de forma interativa:

```bash
.venv/Scripts/jupyter notebook
```

Para reexecutar todas as células e regenerar tabelas e figuras:

```bash
.venv/Scripts/jupyter nbconvert --to notebook --execute --inplace notebooks/analise_quicksort.ipynb
```

Os tempos de execução variam a cada execução, conforme a carga da máquina, portanto, uma reexecução produz tempos diferentes dos apresentados no relatório. Os números de comparações e de trocas são determinísticos e se reproduzem exatamente. O valor de M utilizado nos experimentos é fixado em 8 no notebook, de modo que uma reexecução não altera a configuração das versões comparadas.

## Convenções adotadas

- Uma comparação é contabilizada a cada comparação entre dois elementos.
- Uma troca é contabilizada a cada troca de posição entre dois elementos. A troca de um elemento com ele mesmo (mesma posição) não é realizada nem contabilizada, por isso, no vetor já ordenado com pivô no último elemento, o Quicksort recursivo e o híbrido registram zero trocas.
- Na ordenação por inserção, cada deslocamento de um elemento para a direita é contabilizado como uma troca, a escrita da chave em sua posição final não é contabilizada.
- Na escolha do pivô pela mediana de três, as três comparações e as trocas realizadas na escolha do pivô são contabilizadas, assim como a movimentação do pivô para o último elemento antes da partição.
- O tempo de execução é medido com a função `time.perf_counter`, que utiliza o relógio da máquina.
- As massas de teste são geradas com semente fixa, garantindo que todas as versões e repetições utilizem exatamente os mesmos dados.

## Ambiente dos experimentos

Os resultados apresentados no relatório foram obtidos com Python 3.11.9 no Windows 11 (build 26200). A função `platform.platform()` do Python 3.11 identifica esse sistema como "Windows-10-10.0.26200", porque o Windows 11 mantém a versão interna 10.0, o número de build 26200 corresponde ao Windows 11.

## Correspondência com o relatório

As tabelas e figuras do relatório foram geradas pelo notebook e estão gravadas em `resultados/`. As figuras em `relatorio/figuras/` são cópias idênticas das figuras em `resultados/figuras/`.

| Relatório | Tabela (`resultados/tabelas/`) | Figura (`resultados/figuras/`) |
|---|---|---|
| Tabela 1 e Figura 1: determinação de M (1000 elementos) | `determinacao_m_1000.csv` | `determinacao_m.png` |
| Tabela 2: confirmação de M (10000 elementos) | `determinacao_m_10000.csv` | — |
| Tabela 3 e Figura 2: massa aleatória | `comparativo_aleatorio.csv` | `comparativo_aleatorio.png` |
| Tabela 4 e Figura 3: massa ordenada | `comparativo_ordenado.csv` | `comparativo_ordenado.png` |
| Tabela 5 e Figura 4: massa ordenada inversamente | `comparativo_inverso.csv` | `comparativo_inverso.png` |
| Tabela 6 e Figura 5: massa com muitos repetidos | `comparativo_repetidos.csv` | `comparativo_repetidos.png` |
| Tabela 7 e Figura 6: pior caso forçado | `pior_caso.csv` | `pior_caso.png` |

As Tabelas 8 e 9 do relatório (razões entre tamanhos consecutivos) são calculadas no notebook a partir de `pior_caso.csv`. Os tempos estão em segundos, exceto nos arquivos de determinação de M, em que estão em milissegundos. Os arquivos de determinação de M foram transcritos das saídas gravadas no notebook, que exibem o tempo com seis casas decimais.

## Resultados principais

- O limiar M foi determinado empiricamente como 8, com vetores aleatórios de 1000 elementos e 100 repetições.
- Nas massas ordenada e inversa, o Quicksort recursivo e o híbrido apresentam custo quadrático, com exatamente n(n - 1)/2 comparações no recursivo e poucas comparações a menos no híbrido, enquanto a mediana de três mantém o custo Θ(n log n).
- A massa com muitos elementos repetidos evidencia a fragilidade do particionamento de Lomuto diante de chaves duplicadas.
- O experimento do pior caso forçado confirma o crescimento quadrático do tempo, com razões próximas de 4 ao dobrar o tamanho do vetor.
