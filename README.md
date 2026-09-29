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
- `scripts/`: scripts de apoio para reconstruir o notebook, o documento de achados e o relatório;
- `relatorio/`: projeto LaTeX do relatório final, pronto para compilação no Overleaf (ver `relatorio/LEIA-ME.txt`);
- `ACHADOS.md`: documento com todos os achados do estudo, incluindo metodologia, resultados e análise.

## Como executar

### 1. Ambiente virtual e dependências

Em um terminal na raiz do repositório:

```bash
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
```

No Windows, o executável do ambiente fica em `.venv/Scripts/`; em Linux e macOS, em `.venv/bin/`.

### 2. Testes de correção

```bash
.venv/Scripts/python -m quicksort.teste_correcao
```

### 3. notebook de análises

Para abrir o notebook de forma interativa:

```bash
.venv/Scripts/jupyter notebook
```

Para reexecutar todas as células e regenerar tabelas e figuras:

```bash
.venv/Scripts/jupyter nbconvert --to notebook --execute --inplace notebooks/analise_quicksort.ipynb
```

### 4. Regenerar os artefatos (opcional)

```bash
.venv/Scripts/python scripts/construir_notebook.py
.venv/Scripts/python scripts/aplicar_analise.py
.venv/Scripts/python scripts/gerar_achados.py
.venv/Scripts/python scripts/gerar_relatorio.py
```

## Convenções adotadas

- Uma comparação é contabilizada a cada comparação entre dois elementos.
- Uma troca é contabilizada a cada troca de posição entre dois elementos.
- Na ordenação por inserção, cada deslocamento de um elemento para a direita é contabilizado como uma troca; a escrita da chave em sua posição final não é contabilizada.
- Na escolha do pivô pela mediana de três, as três comparações e as trocas realizadas na escolha do pivô são contabilizadas, assim como a movimentação do pivô para o último elemento antes da partição.
- O tempo de execução é medido com a função `time.perf_counter`, que utiliza o relógio da máquina.
- As massas de teste são geradas com semente fixa, garantindo que todas as versões e repetições utilizem exatamente os mesmos dados.

## Resultados principais

- O limiar M foi determinado empiricamente como 8, com vetores aleatórios de 1000 elementos e 100 repetições.
- Nas massas ordenada e inversa, o Quicksort recursivo e o híbrido apresentam custo quadrático, com exatamente n(n - 1)/2 comparações, enquanto a mediana de três mantém o custo O(n log n).
- A massa com muitos elementos repetidos evidencia a fragilidade do particionamento de Lomuto diante de chaves duplicadas.
- O experimento do pior caso forçado confirma o crescimento quadrático do tempo, com razões próximas de 4 ao dobrar o tamanho do vetor.

Os detalhes completos, com tabelas e análise crítica, estão em `ACHADOS.md`.
