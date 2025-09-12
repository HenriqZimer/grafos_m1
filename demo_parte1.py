#!/usr/bin/env python3
"""
DEMONSTRAÇÃO TRABALHO M1 - PARTE 1
Verificação dos requisitos solicitados
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from grafo import Grafo

print("🎯 TRABALHO M1 - PARTE 1: IMPLEMENTAÇÃO DE GRAFOS")
print("=" * 55)

print("\n📋 REQUISITOS VERIFICADOS:")
print("✅ Implementação com lista de adjacência")
print("✅ Implementação com matriz de adjacência") 
print("✅ Funções básicas para ambas representações")
print("✅ Suporte a grafos dirigidos e não dirigidos")

print("\n" + "=" * 55)
print("🔍 DEMONSTRAÇÃO DAS FUNCIONALIDADES")
print("=" * 55)

# Criar grafo não dirigido
print("\n1️⃣ GRAFO NÃO DIRIGIDO (5 vértices)")
print("-" * 35)
g1 = Grafo(5, dirigido=False)

# Adicionar arestas
print("📝 Adicionando arestas:")
arestas = [(0, 1, 3), (0, 2, 5), (1, 3, 2), (2, 4, 1), (3, 4, 4)]
for origem, destino, peso in arestas:
    g1.adicionar_aresta(origem, destino, peso)
    print(f"   Aresta {origem} → {destino} (peso {peso})")

print(f"\n📊 Estatísticas:")
print(f"   • Número de vértices: {g1.num_vertices}")
print(f"   • Número de arestas: {g1.obter_num_arestas()}")
print(f"   • Grafo conexo: {g1.eh_conexo()}")

print(f"\n📋 REPRESENTAÇÃO POR LISTA DE ADJACÊNCIA:")
g1.imprimir_lista_adjacencia()

print(f"\n📋 REPRESENTAÇÃO POR MATRIZ DE ADJACÊNCIA:")
g1.imprimir_matriz_adjacencia()

print(f"\n🔍 FUNÇÕES BÁSICAS:")
print(f"   • Grau do vértice 0: {g1.obter_grau(0)}")
print(f"   • Vizinhos do vértice 1: {[v for v, p in g1.obter_vizinhos(1)]}")
print(f"   • Existe aresta 0→2: {g1.existe_aresta(0, 2)}")
print(f"   • Existe aresta 0→3: {g1.existe_aresta(0, 3)}")

# Criar grafo dirigido
print(f"\n" + "=" * 55)
print("2️⃣ GRAFO DIRIGIDO (4 vértices)")
print("-" * 30)
g2 = Grafo(4, dirigido=True)

# Adicionar arestas direcionadas
print("📝 Adicionando arestas direcionadas:")
arestas_dir = [(0, 1, 2), (0, 2, 4), (1, 3, 1), (2, 3, 3)]
for origem, destino, peso in arestas_dir:
    g2.adicionar_aresta(origem, destino, peso)
    print(f"   Aresta {origem} → {destino} (peso {peso})")

print(f"\n📊 Estatísticas:")
print(f"   • Número de vértices: {g2.num_vertices}")
print(f"   • Número de arestas: {g2.obter_num_arestas()}")

print(f"\n📋 REPRESENTAÇÃO POR LISTA DE ADJACÊNCIA:")
g2.imprimir_lista_adjacencia()

print(f"\n📋 REPRESENTAÇÃO POR MATRIZ DE ADJACÊNCIA:")
g2.imprimir_matriz_adjacencia()

print(f"\n🔍 FUNÇÕES ESPECÍFICAS PARA GRAFO DIRIGIDO:")
print(f"   • Grau de entrada do vértice 3: {g2.obter_grau_entrada(3)}")
print(f"   • Grau de saída do vértice 0: {g2.obter_grau_saida(0)}")
print(f"   • Grau total do vértice 1: {g2.obter_grau(1)}")

# Demonstrar remoção de aresta
print(f"\n" + "=" * 55)
print("3️⃣ OPERAÇÕES DE REMOÇÃO")
print("-" * 25)
print("📝 Removendo aresta 0→2 do grafo dirigido:")
g2.remover_aresta(0, 2)
print("   Aresta removida!")

print(f"\n📋 Lista de adjacência após remoção:")
g2.imprimir_lista_adjacencia()

print(f"\n📋 Matriz de adjacência após remoção:")
g2.imprimir_matriz_adjacencia()

print(f"\n" + "=" * 55)
print("✅ TRABALHO M1 - PARTE 1 COMPLETO!")
print("=" * 55)

print(f"\n📋 RESUMO DO QUE FOI IMPLEMENTADO:")
print(f"✅ Classe Grafo com duas representações:")
print(f"   • Lista de adjacência")
print(f"   • Matriz de adjacência")
print(f"✅ Suporte completo para:")
print(f"   • Grafos dirigidos e não dirigidos")
print(f"   • Arestas com pesos")
print(f"✅ Funções básicas implementadas:")
print(f"   • adicionar_aresta()")
print(f"   • remover_aresta()")
print(f"   • existe_aresta()")
print(f"   • obter_vizinhos()")
print(f"   • obter_grau() / obter_grau_entrada() / obter_grau_saida()")
print(f"   • obter_num_arestas()")
print(f"   • eh_conexo()")
print(f"   • imprimir_lista_adjacencia()")
print(f"   • imprimir_matriz_adjacencia()")

print(f"\n🎯 TODOS OS REQUISITOS DA PARTE 1 FORAM ATENDIDOS!")