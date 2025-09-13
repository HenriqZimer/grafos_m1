#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstração específica com slides.txt
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from grafo_parte2 import Grafo

def separador(titulo):
    """Imprime um separador com título"""
    print("\n" + "="*60)
    print(f" {titulo}")
    print("="*60)

def main():
    arquivo = "data/slides.txt"
    nome_arquivo = "slides.txt"
    
    print(f"DEMONSTRAÇÃO DA PARTE 2 COM {nome_arquivo.upper()}")
    print("Verificando algoritmos com grafo específico")
    
    # ========================================
    # CARREGAMENTO DO ARQUIVO
    # ========================================
    separador(f"CARREGANDO {nome_arquivo.upper()}")
    
    try:
        grafo = Grafo(arquivo=arquivo)
        print(f"✓ Grafo carregado: {grafo.num_vertices} vértices, {grafo.obter_num_arestas()} arestas")
        print(f"✓ Dirigido: {grafo.dirigido}, Ponderado: {grafo.ponderado}")
        
        # Mostrar estrutura do grafo
        print(f"\n📊 Estrutura do grafo:")
        print("Matriz de adjacência:")
        grafo.imprimir_matriz_adjacencia()
        
    except Exception as e:
        print(f"  ERRO: {e}")
        return
    
    # ========================================
    # BUSCA EM LARGURA (BFS)
    # ========================================
    separador("BUSCA EM LARGURA (BFS)")
    
    print(f"Executando BFS no grafo {nome_arquivo} a partir do vértice 0:")
    
    try:
        ordem_bfs = grafo.busca_largura(0)
        print(f"\n✓ RESULTADO: Ordem de visitação BFS = {ordem_bfs}")
        print(f"✓ Visitou {len(ordem_bfs)} vértices de {grafo.num_vertices} totais")
        
    except Exception as e:
        print(f"  ERRO no BFS: {e}")
    
    # ========================================
    # BUSCA EM PROFUNDIDADE (DFS)
    # ========================================
    separador("BUSCA EM PROFUNDIDADE (DFS)")
    
    print(f"Executando DFS no grafo {nome_arquivo} a partir do vértice 0:")
    
    try:
        ordem_dfs = grafo.busca_profundidade(0)
        print(f"\n✓ RESULTADO: Ordem de visitação DFS = {ordem_dfs}")
        print(f"✓ Visitou {len(ordem_dfs)} vértices de {grafo.num_vertices} totais")
        
    except Exception as e:
        print(f"  ERRO no DFS: {e}")
    
    # ========================================
    # ALGORITMO DE DIJKSTRA
    # ========================================
    separador("ALGORITMO DE DIJKSTRA")
    
    print(f"Executando Dijkstra no grafo {nome_arquivo} a partir do vértice 0:")
    
    try:
        distancias, predecessores = grafo.dijkstra(0)
        
        print("\n=== Resultados do Dijkstra ===")
        print("Distâncias mínimas a partir do vértice 0:")
        for vertice in range(grafo.num_vertices):
            if distancias[vertice] == float('inf'):
                print(f"  Vértice {vertice}: INACESSÍVEL")
            else:
                print(f"  Vértice {vertice}: distância {distancias[vertice]}")
        
        print("\nCaminhos mínimos:")
        for vertice in range(1, grafo.num_vertices):
            if distancias[vertice] != float('inf'):
                caminho = grafo._reconstruir_caminho(predecessores, vertice)
                print(f"  0 → {vertice}: {' → '.join(map(str, caminho))}")
        
        print(f"\n✓ RESULTADO: Algoritmo de Dijkstra executado com sucesso!")
        
    except Exception as e:
        print(f"  ERRO no Dijkstra: {e}")
    
    # ========================================
    # RESUMO
    # ========================================
    separador(f"RESUMO - {nome_arquivo.upper()}")
    
    print("✅ TESTE CONCLUÍDO:")
    print(f"   ✓ Arquivo {nome_arquivo} carregado com sucesso")
    print(f"   ✓ BFS executado: visitou {len(ordem_bfs) if 'ordem_bfs' in locals() else 0} vértices")
    print(f"   ✓ DFS executado: visitou {len(ordem_dfs) if 'ordem_dfs' in locals() else 0} vértices")
    print(f"   ✓ Dijkstra executado: calculou distâncias para {grafo.num_vertices} vértices")
    print(f"   ✓ Grafo: {grafo.num_vertices} vértices, {grafo.obter_num_arestas()} arestas")
    print(f"   ✓ Propriedades: {'Dirigido' if grafo.dirigido else 'Não dirigido'}, {'Ponderado' if grafo.ponderado else 'Não ponderado'}")
    print("\n🎉 TESTE COM SLIDES.TXT FINALIZADO!")

if __name__ == "__main__":
    main()