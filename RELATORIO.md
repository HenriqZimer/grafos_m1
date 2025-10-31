# Relatório de Resultados - Trabalho de Grafos (Módulo 2)

---

## Sumário
1. [Introdução](#introdução)
2. [Árvore Geradora Mínima (MST)](#árvore-geradora-mínima-mst)
3. [Coloração de Grafos](#coloração-de-grafos)
4. [Análise Comparativa](#análise-comparativa)
5. [Conclusões](#conclusões)

---

## Introdução

Este relatório apresenta os resultados da execução de algoritmos de **Árvore Geradora Mínima (MST)** e **Coloração de Grafos** em diversas instâncias de teste. Os algoritmos foram implementados em Python e executados nas instâncias fornecidas pelo professor.

**Algoritmos implementados:**
- **MST:** Kruskal e Prim
- **Coloração:** Welsh-Powell, DSATUR e Heurística Simples Gulosa

---

## 1. Árvore Geradora Mínima (MST)

### 1.1. Resultados Detalhados

#### Instância: 50vertices25%Arestas.txt
- **Vértices:** 50
- **Arestas:** 304

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 5339             | 0.000346 s        |
| Prim      | 5339             | 0.000130 s        |

---

#### Instância: 50vertices50%Arestas.txt
- **Vértices:** 50
- **Arestas:** 603

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 2770             | 0.000736 s        |
| Prim      | 2770             | 0.000133 s        |

---

#### Instância: 50vertices100%Arestas.txt
- **Vértices:** 50
- **Arestas:** 1225

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 867              | 0.001449 s        |
| Prim      | 867              | 0.000225 s        |

---

#### Instância: 500vertices25%Arestas.txt
- **Vértices:** 500
- **Arestas:** 31130

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 4684             | 0.044594 s        |
| Prim      | 4684             | 0.013250 s        |

---

#### Instância: 500vertices50%Arestas.txt
- **Vértices:** 500
- **Arestas:** 62416

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 2155             | 0.096626 s        |
| Prim      | 2155             | 0.021384 s        |

---

#### Instância: 500vertices100%Arestas.txt
- **Vértices:** 500
- **Arestas:** 124750

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 894              | 0.206844 s        |
| Prim      | 894              | 0.032227 s        |

---

#### Instância: 1000vertices25%Arestas.txt
- **Vértices:** 1000
- **Arestas:** 125117

| Algoritmo | Peso Total da MST | Tempo de Execução |
|-----------|-------------------|-------------------|
| Kruskal   | 4112             | 0.278131 s        |
| Prim      | 4112             | 0.067010 s        |

---

### 1.2. Tabela Resumo - MST

| Instância                    | Vértices | Arestas | Peso Total (MST) | Kruskal (s) | Prim (s) | Mais Rápido |
|------------------------------|----------|---------|------------------|-------------|----------|-------------|
| 50vertices25%Arestas.txt     | 50       | 304     | 5339            | 0.000346    | 0.000130 | **Prim**    |
| 50vertices50%Arestas.txt     | 50       | 603     | 2770            | 0.000736    | 0.000133 | **Prim**    |
| 50vertices100%Arestas.txt    | 50       | 1225    | 867             | 0.001449    | 0.000225 | **Prim**    |
| 500vertices25%Arestas.txt    | 500      | 31130   | 4684            | 0.044594    | 0.013250 | **Prim**    |
| 500vertices50%Arestas.txt    | 500      | 62416   | 2155            | 0.096626    | 0.021384 | **Prim**    |
| 500vertices100%Arestas.txt   | 500      | 124750  | 894             | 0.206844    | 0.032227 | **Prim**    |
| 1000vertices25%Arestas.txt   | 1000     | 125117  | 4112            | 0.278131    | 0.067010 | **Prim**    |

---

## 2. Coloração de Grafos

### 2.1. Resultados Detalhados

#### Instância: k33.txt (Grafo Bipartido Completo K₃,₃)
- **Vértices:** 6
- **Arestas:** 9
- **Descrição:** Grafo bipartido completo

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| Welsh-Powell        | 2               | 0.000016 s        |
| DSATUR              | 2               | 0.000026 s        |
| Heurística Simples  | 2               | 0.000023 s        |

✅ **Resultado:** Todos os algoritmos encontraram a solução ótima (2 cores para grafo bipartido)

---

#### Instância: k5.txt (Grafo Completo K₅)
- **Vértices:** 5
- **Arestas:** 10
- **Descrição:** Grafo completo com 5 vértices

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| Welsh-Powell        | 5               | 0.000011 s        |
| DSATUR              | 5               | 0.000026 s        |
| Heurística Simples  | 5               | 0.000010 s        |

✅ **Resultado:** Todos os algoritmos encontraram a solução ótima (5 cores - número cromático de K₅)

---

#### Instância: kquase5.txt
- **Vértices:** 5
- **Arestas:** 9
- **Descrição:** K₅ com uma aresta removida

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| Welsh-Powell        | 4               | 0.000010 s        |
| DSATUR              | 4               | 0.000014 s        |
| Heurística Simples  | 4               | 0.000005 s        |

✅ **Resultado:** Todos os algoritmos encontraram a solução ótima (4 cores)

---

#### Instância: r250-66-65.txt
- **Vértices:** 250
- **Arestas:** 13909

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| Welsh-Powell        | 68              | 0.003997 s        |
| **DSATUR**          | **67**          | 0.010122 s        |
| Heurística Simples  | 75              | 0.002831 s        |

🏆 **Melhor resultado:** DSATUR com 67 cores

---

#### Instância: r1000-234-234.txt
- **Vértices:** 1000
- **Arestas:** 238267

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| Welsh-Powell        | 259             | 0.090380 s        |
| **DSATUR**          | **250**         | 0.198854 s        |
| Heurística Simples  | 275             | 0.062038 s        |

🏆 **Melhor resultado:** DSATUR com 250 cores

---

#### Instância: C4000-260-X.txt
- **Vértices:** 4000
- **Arestas:** 4000268
- **Descrição:** Grafo muito denso

| Algoritmo            | Número de Cores | Tempo de Execução |
|---------------------|-----------------|-------------------|
| **Welsh-Powell**    | **394**         | 2.065922 s        |
| DSATUR              | 401             | 4.445622 s        |
| Heurística Simples  | 402             | 1.327213 s        |

🏆 **Melhor resultado:** Welsh-Powell com 394 cores

---

### 2.2. Tabela Resumo - Coloração

| Instância          | Vértices | Arestas  | Welsh-Powell | DSATUR | Heur. Simples | Melhor Resultado | Algoritmo Vencedor |
|--------------------|----------|----------|--------------|--------|---------------|------------------|--------------------|
| k33.txt            | 6        | 9        | 2            | 2      | 2             | **2**            | Empate (ótimo)     |
| k5.txt             | 5        | 10       | 5            | 5      | 5             | **5**            | Empate (ótimo)     |
| kquase5.txt        | 5        | 9        | 4            | 4      | 4             | **4**            | Empate (ótimo)     |
| r250-66-65.txt     | 250      | 13909    | 68           | **67** | 75            | **67**           | **DSATUR**         |
| r1000-234-234.txt  | 1000     | 238267   | 259          | **250**| 275           | **250**          | **DSATUR**         |
| C4000-260-X.txt    | 4000     | 4000268  | **394**      | 401    | 402           | **394**          | **Welsh-Powell**   |

---

## 3. Análise Comparativa

### 3.1. MST - Kruskal vs Prim

**Observações:**
- O algoritmo de **Prim foi mais rápido** em **todas as instâncias** testadas
- A diferença de desempenho aumenta com grafos mais densos
- Ambos os algoritmos encontram sempre o mesmo peso total (solução ótima)

**Análise de complexidade:**
- **Kruskal:** O(E log E) - depende principalmente do número de arestas
- **Prim:** O(V²) na implementação simples - depende do número de vértices

**Por que Prim foi mais rápido?**
- Grafos testados são relativamente densos (muitas arestas)
- Prim trabalha melhor em grafos densos
- Implementação de Prim com busca simples foi eficiente para esses tamanhos

---

### 3.2. Coloração - Comparação de Algoritmos

**Resultados por categoria:**

1. **Grafos Pequenos (k33, k5, kquase5):**
   - Todos os algoritmos encontraram a solução ótima
   - Diferenças de tempo desprezíveis (< 0.001s)

2. **Grafos Médios (r250-66-65.txt, r1000-234-234.txt):**
   - **DSATUR** obteve os melhores resultados
   - DSATUR encontrou 9 cores a menos que Welsh-Powell em r1000
   - Heurística Simples foi a mais rápida, mas com piores resultados

3. **Grafo Grande Denso (C4000-260-X.txt):**
   - **Welsh-Powell** obteve o melhor resultado (394 cores)
   - Welsh-Powell também teve tempo intermediário
   - DSATUR foi o mais lento e com pior resultado

**Análise:**
- **Welsh-Powell:** Excelente para grafos muito densos, ordena por grau decrescente
- **DSATUR:** Melhor para grafos de tamanho médio, considera saturação dos vértices
- **Heurística Simples:** Mais rápida, mas geralmente piores resultados (boa para soluções rápidas)

---

## 4. Conclusões

### 4.1. Árvore Geradora Mínima

1. **Ambos os algoritmos são corretos:** Kruskal e Prim sempre encontraram o mesmo peso total
2. **Prim teve melhor desempenho:** Em todos os casos testados
3. **Escalabilidade:** Prim escalou melhor para grafos maiores e mais densos
4. **Uso prático:** Para grafos densos, Prim é preferível; para grafos esparsos, Kruskal pode ser melhor

### 4.2. Coloração de Grafos

1. **Não existe um "melhor" algoritmo universal:**
   - Welsh-Powell: Melhor em grafos muito densos
   - DSATUR: Melhor em grafos de tamanho médio
   - Heurística Simples: Mais rápida quando qualidade não é crítica

2. **Trade-off tempo vs qualidade:**
   - Heurística Simples é mais rápida mas com piores resultados
   - DSATUR geralmente encontra melhores soluções mas é mais lento

3. **Instâncias conhecidas:**
   - Todos os algoritmos encontraram soluções ótimas para K₃,₃, K₅ e quase-K₅

### 4.3. Considerações Finais

- A implementação em Python com lista de adjacências foi adequada para os tamanhos testados
- Os algoritmos de MST são exatos e sempre encontram a solução ótima
- Os algoritmos de coloração são heurísticos e não garantem o ótimo, mas fornecem boas aproximações
- A escolha do algoritmo deve considerar o tipo de grafo (denso/esparso) e os requisitos (tempo/qualidade)

---

## Anexos

### Arquivos do Projeto
- `mst.py` - Implementação dos algoritmos de MST (Kruskal e Prim)
- `coloracao_grafos.py` - Implementação dos algoritmos de coloração
- `executar_testes.py` - Script para executar todos os testes
- `relatorio_resultados.txt` - Relatório completo em formato texto

### Como Executar
```bash
python3 executar_testes.py
```

Este comando executa todos os testes e gera o relatório automaticamente.

---

**Fim do Relatório**
