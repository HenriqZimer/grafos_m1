# 📊 Trabalhos M1 - Teoria dos Grafos

Implementação completa dos trabalhos M1 de **Teoria dos Grafos** em Python, organizados em uma estrutura de projeto bem definida.

## 📁 Estrutura do Projeto

```
Grafos/
├── src/                        # 💻 Código fonte
│   ├── grafo.py               # Implementação Parte 1
│   └── grafo_parte2.py        # Implementação Parte 2 + Algoritmos
├── tests/                      # 🧪 Testes
│   ├── testes_grafo.py        # Testes da Parte 1
│   └── testes_parte2.py       # Testes da Parte 2
├── examples/                   # 📋 Exemplos práticos
│   └── exemplos_praticos.py   # Casos de uso reais
├── data/                       # 📂 Arquivos de dados
│   ├── grafo_ponderado.txt    # Grafo com pesos
│   ├── grafo_dirigido.txt     # Grafo direcionado
│   └── grafo_simples.txt      # Grafo básico
├── docs/                       # 📚 Documentação
│   ├── README.md              # Este arquivo
│   ├── AUTOMACAO.md           # Guia de automação
│   └── relatorio_executivo.py # Relatório do projeto
└── Makefile                   # 🛠️ Automação
```

## 🚀 Execução Rápida

### Executar Tudo
```bash
wsl bash -c "cd /mnt/c/Users/henrique.zimermann/Documents/Grafos && make"
```

### Comandos Específicos
```bash
# Navegar para a pasta no WSL
cd /mnt/c/Users/henrique.zimermann/Documents/Grafos

# Executar comandos específicos
make teste1      # Testes da Parte 1
make teste2      # Testes da Parte 2  
make exemplos    # Exemplos práticos
make estrutura   # Mostra a estrutura
make help        # Ajuda completa
```

## 📋 Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| `make` | Executa tudo (padrão) |
| `make teste1` | Testes da Parte 1 |
| `make teste2` | Testes da Parte 2 |
| `make testes` | Todos os testes |
| `make exemplos` | Exemplos práticos |
| `make parte1` | Executa Parte 1 |
| `make parte2` | Executa Parte 2 |
| `make demo` | Demonstração |
| `make relatorio` | Relatório executivo |
| `make validar` | Validação completa |
| `make structure` | Mostra estrutura |
| `make help` | Ajuda completa |

## 🎯 Implementações

### **Parte 1** - Implementação Básica (`src/grafo.py`)
- ✅ Representação por **lista de adjacência**
- ✅ Representação por **matriz de adjacência**
- ✅ Operações básicas (adicionar, remover, verificar)
- ✅ Análise de graus e conectividade
- ✅ Suporte para grafos **dirigidos** e **não dirigidos**

### **Parte 2** - Algoritmos Avançados (`src/grafo_parte2.py`)
- ✅ **Leitura de arquivos** (formato especificado)
- ✅ **Busca em Largura (BFS)** - exploração por níveis
- ✅ **Busca em Profundidade (DFS)** - exploração recursiva
- ✅ **Algoritmo de Dijkstra** - caminhos mínimos com reconstrução
- ✅ Suporte para grafos **ponderados** e **não ponderados**

## 📊 Exemplos de Uso

### Rede Social
```python
# Modelagem de amizades (grafo não dirigido)
g = Grafo(6, dirigido=False)
g.adicionar_aresta(0, 1)  # Alice - Bob
g.adicionar_aresta(1, 2)  # Bob - Carol
```

### Mapa de Cidades
```python
# Distâncias entre cidades (grafo ponderado)
g = Grafo(4, dirigido=False, ponderado=True)
g.adicionar_aresta(0, 1, 430)  # SP - RJ: 430km
```

### Fluxo de Trabalho
```python
# Dependências de tarefas (grafo dirigido)
g = Grafo(4, dirigido=True)
g.adicionar_aresta(0, 1)  # Análise → Design
```

## 🧪 Testes

### Testes da Parte 1 (`tests/testes_grafo.py`)
- Grafos simples e complexos
- Operações básicas
- Casos extremos
- Benchmark de representações

### Testes da Parte 2 (`tests/testes_parte2.py`)
- Leitura de arquivos
- Algoritmos de busca (BFS, DFS)
- Algoritmo de Dijkstra
- Grafos desconexos
- Teste de performance

## 📂 Formato dos Arquivos de Dados

```
5 false true          # vértices dirigido ponderado
0 1 4.0               # origem destino peso
1 2 1.0
2 3 8.0
# ... mais arestas
```

## 🛠️ Requisitos

- **WSL** (Windows Subsystem for Linux)
- **Python 3** 
- **make** (geralmente já incluído no WSL)

## 🔧 Instalação

1. Verifique se o WSL está instalado
2. Instale dependências (se necessário):
   ```bash
   make install-deps
   ```

## 📈 Performance

- **BFS/DFS**: O(V + E) - Linear nos vértices e arestas
- **Dijkstra**: O((V + E) log V) - Com heap binário
- **Memória**: Lista de adjacência mais eficiente para grafos esparsos

## 🎓 Aplicações Acadêmicas

Este projeto implementa:
- **Estruturas de dados** fundamentais
- **Algoritmos clássicos** de grafos
- **Análise de complexidade**
- **Casos de teste** abrangentes
- **Documentação** completa

## 🔍 Validação

Execute `make validar` para uma verificação completa:
- ✅ Todos os testes
- ✅ Exemplos práticos  
- ✅ Relatório executivo
- ✅ Verificação de dependências

---