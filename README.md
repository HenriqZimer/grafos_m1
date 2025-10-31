# Trabalho de Grafos - Módulo 2

## 📋 Descrição

Implementação de algoritmos para **Árvore Geradora Mínima (MST)** e **Coloração de Grafos** em Python, desenvolvido como trabalho acadêmico da disciplina de Grafos.

## 🎯 Objetivos

- Implementar e comparar algoritmos de MST (Kruskal e Prim)
- Implementar e comparar algoritmos de coloração de grafos (Welsh-Powell, DSATUR e Heurística Simples)
- Executar testes em diversas instâncias
- Gerar relatório com análise comparativa de desempenho

## 🏗️ Estrutura do Projeto

```
grafos_m1/
├── aresta.py                 # Classe Aresta
├── grafo.py                  # Classe base Grafo
├── grafo_lista.py            # Implementação com lista de adjacências
├── grafo_matriz.py           # Implementação com matriz de adjacências
├── mst.py                    # Algoritmos de MST (Kruskal e Prim)
├── coloracao_grafos.py       # Algoritmos de coloração
├── executar_testes.py        # Script principal de testes
├── busca_largura.py          # Busca em largura (BFS)
├── busca_profundidade.py     # Busca em profundidade (DFS)
├── dijkstra.py               # Algoritmo de Dijkstra
├── arquivos_m2/
│   ├── MST/                  # Instâncias para testes de MST
│   │   ├── 50vertices25%Arestas.txt
│   │   ├── 50vertices50%Arestas.txt
│   │   ├── 50vertices100%Arestas.txt
│   │   ├── 500vertices25%Arestas.txt
│   │   ├── 500vertices50%Arestas.txt
│   │   ├── 500vertices100%Arestas.txt
│   │   └── 1000vertices25%Arestas.txt
│   └── coloracao/            # Instâncias para testes de coloração
│       ├── k33.txt
│       ├── k5.txt
│       ├── kquase5.txt
│       ├── r250-66-65.txt
│       ├── r1000-234-234.txt
│       └── C4000-260-X.txt
├── RELATORIO.md              # Relatório completo em Markdown
└── relatorio_resultados.txt  # Relatório gerado automaticamente
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior

### Executar todos os testes

```bash
python3 executar_testes.py
```

Este comando irá:
1. Executar algoritmos de MST em todas as instâncias da pasta `arquivos_m2/MST/`
2. Executar algoritmos de coloração em todas as instâncias da pasta `arquivos_m2/coloracao/`
3. Gerar automaticamente o arquivo `relatorio_resultados.txt` com os resultados

### Usar os algoritmos individualmente

#### Exemplo: MST com Kruskal

```python
from grafo_lista import GrafoLista
from mst import MST

# Carregar grafo
grafo = GrafoLista(direcionado=False, ponderado=True)
grafo.ler_arquivo('arquivos_m2/MST/50vertices25%Arestas.txt')

# Executar Kruskal
mst = MST(grafo)
peso_total = mst.kruskal()
mst.imprimir_resultado(mostrar_arestas=True)
```

#### Exemplo: Coloração com Welsh-Powell

```python
from grafo_lista import GrafoLista
from coloracao_grafos import ColoracaoGrafos

# Carregar grafo
grafo = GrafoLista(direcionado=False, ponderado=False)
grafo.ler_arquivo('arquivos_m2/coloracao/k5.txt')

# Executar Welsh-Powell
coloracao = ColoracaoGrafos(grafo)
num_cores = coloracao.welsh_powell()
coloracao.imprimir_resultado(mostrar_cores=True)
```

## 📊 Algoritmos Implementados

### Árvore Geradora Mínima (MST)

1. **Kruskal**
   - Complexidade: O(E log E)
   - Baseado em ordenação de arestas
   - Usa estrutura Union-Find

2. **Prim**
   - Complexidade: O(V²) (implementação simples)
   - Cresce a árvore a partir de um vértice inicial
   - Melhor para grafos densos

### Coloração de Grafos

1. **Welsh-Powell**
   - Heurística gulosa
   - Ordena vértices por grau decrescente
   - Atribui cores sequencialmente

2. **DSATUR**
   - Heurística mais sofisticada
   - Considera grau de saturação dos vértices
   - Geralmente melhores resultados que Welsh-Powell

3. **Heurística Simples Gulosa**
   - Abordagem mais simples e rápida
   - Processa vértices na ordem original
   - Boa para soluções rápidas

## 📈 Resultados Principais

### MST
- **Prim foi mais rápido em todas as instâncias testadas**
- Ambos os algoritmos sempre encontram a solução ótima
- Diferença de desempenho aumenta com grafos mais densos

### Coloração
- **Welsh-Powell:** Melhor para grafos muito densos (ex: C4000)
- **DSATUR:** Melhor para grafos médios (ex: r1000, r250)
- **Heurística Simples:** Mais rápida, mas resultados inferiores

Veja o [RELATORIO.md](RELATORIO.md) para análise completa.

## 📝 Formato dos Arquivos de Entrada

### Para grafos ponderados (MST):
```
<num_vertices> <num_arestas> <direcionado> <ponderado>
<origem> <destino> <peso>
<origem> <destino> <peso>
...
```

Exemplo:
```
4 5 0 1
0 1 10
0 2 15
1 2 20
1 3 25
2 3 30
```

### Para grafos não ponderados (Coloração):
```
<num_vertices> <num_arestas> <direcionado> <ponderado>
<origem> <destino>
<origem> <destino>
...
```

Exemplo:
```
5 10 0 0
0 1
0 2
0 3
...
```

## 🔧 Funcionalidades Adicionais

- Busca em Largura (BFS)
- Busca em Profundidade (DFS)
- Algoritmo de Dijkstra para caminhos mínimos
- Suporte para grafos direcionados e não direcionados
- Suporte para grafos ponderados e não ponderados
- Implementação com lista e matriz de adjacências

## 📖 Documentação

- [RELATORIO.md](RELATORIO.md) - Relatório completo com análise detalhada
- [relatorio_resultados.txt](relatorio_resultados.txt) - Resultados brutos dos testes

## 👨‍💻 Autor

[Seu Nome]

## 📅 Data

31 de Outubro de 2025
