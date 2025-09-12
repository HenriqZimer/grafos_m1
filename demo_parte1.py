#!/usr/bin/env python3
"""
Demo - Parte 1: Demonstração das funcionalidades básicas de grafos
Conforme especificações dos slides S02 - Conceitos Básicos e Representação

Funcionalidades demonstradas:
- Classe base Grafo com construtor direcionado/ponderado
- Especialização GrafoMatriz (matriz de adjacência)
- Especialização GrafoLista (lista de adjacência + estrutura Aresta)
- Todas as funções: inserirVertice, removerVertice, labelVertice, 
  imprimeGrafo, inserirAresta, removerAresta, existeAresta

Autor: Henrique Zimermann
Data: 12 de setembro de 2025
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from grafo import Grafo, GrafoMatriz, GrafoLista, Aresta


def demonstrar_construtor():
    """Demonstra o construtor conforme especificações dos slides"""
    print("="*80)
    print("DEMONSTRAÇÃO 1: CONSTRUTORES CONFORME SLIDES S02")
    print("="*80)
    
    print("\n🏗️  Criando grafos com diferentes configurações:")
    print("\n1. GrafoMatriz - Não direcionado, Não ponderado:")
    grafo1 = GrafoMatriz(direcionado=False, ponderado=False)
    print(f"   ✓ Criado: direcionado={grafo1.direcionado}, ponderado={grafo1.ponderado}")
    
    print("\n2. GrafoLista - Direcionado, Ponderado:")
    grafo2 = GrafoLista(direcionado=True, ponderado=True)
    print(f"   ✓ Criado: direcionado={grafo2.direcionado}, ponderado={grafo2.ponderado}")
    
    print("\n3. GrafoMatriz - Direcionado, Não ponderado:")
    grafo3 = GrafoMatriz(direcionado=True, ponderado=False)
    print(f"   ✓ Criado: direcionado={grafo3.direcionado}, ponderado={grafo3.ponderado}")
    
    print("\n4. GrafoLista - Não direcionado, Ponderado:")
    grafo4 = GrafoLista(direcionado=False, ponderado=True)
    print(f"   ✓ Criado: direcionado={grafo4.direcionado}, ponderado={grafo4.ponderado}")


def demonstrar_vertices():
    """Demonstra operações com vértices"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 2: OPERAÇÕES COM VÉRTICES")
    print("="*80)
    
    print("\n🔵 Testando inserirVertice() e labelVertice():")
    
    # Teste com GrafoMatriz
    print("\n📊 GrafoMatriz:")
    grafo_matriz = GrafoMatriz(direcionado=False, ponderado=False)
    
    vertices = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"]
    print(f"   Inserindo vértices: {vertices}")
    
    for i, vertice in enumerate(vertices):
        sucesso = grafo_matriz.inserirVertice(vertice)
        print(f"   ✓ inserirVertice('{vertice}'): {sucesso}")
    
    print("\n   Labels dos vértices inseridos:")
    for i in range(len(vertices)):
        label = grafo_matriz.labelVertice(i)
        print(f"   - labelVertice({i}): '{label}'")
    
    # Teste com GrafoLista  
    print("\n📋 GrafoLista:")
    grafo_lista = GrafoLista(direcionado=True, ponderado=True)
    
    cidades = ["A", "B", "C"]
    print(f"   Inserindo vértices: {cidades}")
    
    for cidade in cidades:
        sucesso = grafo_lista.inserirVertice(cidade)
        print(f"   ✓ inserirVertice('{cidade}'): {sucesso}")
    
    print("\n   Labels dos vértices inseridos:")
    for i in range(len(cidades)):
        label = grafo_lista.labelVertice(i)
        print(f"   - labelVertice({i}): '{label}'")
    
    # Teste de inserção duplicada
    print("\n🚫 Testando inserção de vértice duplicado:")
    sucesso = grafo_matriz.inserirVertice("São Paulo")
    print(f"   inserirVertice('São Paulo') novamente: {sucesso} (deve ser False)")
    
    return grafo_matriz, grafo_lista


def demonstrar_arestas(grafo_matriz, grafo_lista):
    """Demonstra operações com arestas"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 3: OPERAÇÕES COM ARESTAS")
    print("="*80)
    
    print("\n🔗 Testando inserirAresta(), existeAresta() e removerAresta():")
    
    # Teste com GrafoMatriz (não direcionado, não ponderado)
    print("\n📊 GrafoMatriz (não direcionado, não ponderado):")
    print("   Inserindo arestas entre cidades:")
    
    arestas = [
        (0, 1, "São Paulo - Rio de Janeiro"),
        (0, 2, "São Paulo - Belo Horizonte"), 
        (1, 3, "Rio de Janeiro - Salvador"),
        (2, 3, "Belo Horizonte - Salvador")
    ]
    
    for origem, destino, descricao in arestas:
        sucesso = grafo_matriz.inserirAresta(origem, destino)
        print(f"   ✓ inserirAresta({origem}, {destino}): {sucesso} ({descricao})")
    
    print("\n   Verificando existência das arestas:")
    for origem, destino, descricao in arestas:
        existe = grafo_matriz.existeAresta(origem, destino)
        print(f"   - existeAresta({origem}, {destino}): {existe} ({descricao})")
    
    print("\n   Verificando simetria (grafo não direcionado):")
    for origem, destino, descricao in arestas:
        existe_volta = grafo_matriz.existeAresta(destino, origem)
        print(f"   - existeAresta({destino}, {origem}): {existe_volta} (volta de {descricao})")
    
    # Teste com GrafoLista (direcionado, ponderado)
    print("\n📋 GrafoLista (direcionado, ponderado):")
    print("   Inserindo arestas com pesos:")
    
    arestas_ponderadas = [
        (0, 1, 100, "A -> B (peso 100)"),
        (0, 2, 150, "A -> C (peso 150)"),
        (1, 2, 75, "B -> C (peso 75)")
    ]
    
    for origem, destino, peso, descricao in arestas_ponderadas:
        sucesso = grafo_lista.inserirAresta(origem, destino, peso)
        print(f"   ✓ inserirAresta({origem}, {destino}, {peso}): {sucesso} ({descricao})")
    
    print("\n   Verificando existência das arestas:")
    for origem, destino, peso, descricao in arestas_ponderadas:
        existe = grafo_lista.existeAresta(origem, destino)
        print(f"   - existeAresta({origem}, {destino}): {existe} ({descricao})")
    
    print("\n   Verificando assimetria (grafo direcionado):")
    for origem, destino, peso, descricao in arestas_ponderadas:
        existe_volta = grafo_lista.existeAresta(destino, origem)
        print(f"   - existeAresta({destino}, {origem}): {existe_volta} (volta de {descricao})")
    
    # Teste de remoção
    print("\n🗑️  Testando remoção de arestas:")
    print("   Removendo aresta São Paulo - Rio de Janeiro (0-1) do GrafoMatriz:")
    print(f"   Antes: existeAresta(0, 1) = {grafo_matriz.existeAresta(0, 1)}")
    sucesso = grafo_matriz.removerAresta(0, 1)
    print(f"   removerAresta(0, 1): {sucesso}")
    print(f"   Depois: existeAresta(0, 1) = {grafo_matriz.existeAresta(0, 1)}")
    print(f"   Depois: existeAresta(1, 0) = {grafo_matriz.existeAresta(1, 0)} (simetria)")


def demonstrar_impressao(grafo_matriz, grafo_lista):
    """Demonstra a função imprimeGrafo()"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 4: FUNÇÃO imprimeGrafo()")
    print("="*80)
    
    print("\n🖨️  Imprimindo representações dos grafos:")
    
    print("\n📊 GrafoMatriz:")
    grafo_matriz.imprimeGrafo()
    
    print("\n📋 GrafoLista:")
    grafo_lista.imprimeGrafo()


def demonstrar_remocao_vertices():
    """Demonstra remoção de vértices"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 5: REMOÇÃO DE VÉRTICES")
    print("="*80)
    
    print("\n🗑️  Testando removerVertice():")
    
    # Criar um grafo pequeno para demonstração
    print("\n📊 Criando GrafoMatriz para teste:")
    grafo = GrafoMatriz(direcionado=False, ponderado=False)
    
    vertices = ["X", "Y", "Z"]
    for v in vertices:
        grafo.inserirVertice(v)
    
    # Adicionar algumas arestas
    grafo.inserirAresta(0, 1)  # X-Y
    grafo.inserirAresta(1, 2)  # Y-Z
    grafo.inserirAresta(0, 2)  # X-Z
    
    print("   Grafo inicial:")
    grafo.imprimeGrafo()
    
    # Remover vértice do meio
    print("\n   Removendo vértice Y (índice 1):")
    print(f"   Antes: labelVertice(1) = '{grafo.labelVertice(1)}'")
    sucesso = grafo.removerVertice(1)
    print(f"   removerVertice(1): {sucesso}")
    
    print("\n   Grafo após remoção:")
    grafo.imprimeGrafo()
    
    print("\n   Verificação dos labels restantes:")
    for i in range(len(grafo.vertices)):
        label = grafo.labelVertice(i)
        print(f"   - labelVertice({i}): '{label}'")


def demonstrar_estrutura_aresta():
    """Demonstra a estrutura Aresta auxiliar"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 6: ESTRUTURA ARESTA AUXILIAR")
    print("="*80)
    
    print("\n🏗️  Testando estrutura Aresta:")
    
    # Criar algumas arestas
    aresta1 = Aresta(5, 10)
    aresta2 = Aresta(3)  # peso padrão
    
    print(f"   Aresta(5, 10): destino={aresta1.destino}, peso={aresta1.peso}")
    print(f"   Aresta(3): destino={aresta2.destino}, peso={aresta2.peso}")
    print(f"   str(aresta1): {str(aresta1)}")
    print(f"   str(aresta2): {str(aresta2)}")
    
    # Mostrar como é usada no GrafoLista
    print("\n📋 Uso da estrutura Aresta no GrafoLista:")
    grafo = GrafoLista(direcionado=True, ponderado=True)
    
    # Inserir vértices
    for v in ["Node1", "Node2", "Node3"]:
        grafo.inserirVertice(v)
    
    # Inserir arestas
    grafo.inserirAresta(0, 1, 50)
    grafo.inserirAresta(0, 2, 75)
    
    print("   Estrutura interna das listas:")
    for i, lista_adj in enumerate(grafo.listas):
        label = grafo.labelVertice(i)
        arestas_str = [str(aresta) for aresta in lista_adj]
        print(f"   {label} (índice {i}): {arestas_str}")


def demonstrar_comparacao_representacoes():
    """Demonstra diferenças entre matriz e lista de adjacência"""
    print("\n\n" + "="*80)
    print("DEMONSTRAÇÃO 7: COMPARAÇÃO ENTRE REPRESENTAÇÕES")
    print("="*80)
    
    print("\n⚖️  Criando o mesmo grafo com ambas as representações:")
    
    # Configuração comum
    vertices = ["Hub", "Norte", "Sul", "Leste", "Oeste"]
    arestas = [(0, 1, 10), (0, 2, 15), (0, 3, 12), (0, 4, 8), (1, 3, 5)]
    
    # GrafoMatriz
    matriz = GrafoMatriz(direcionado=True, ponderado=True)
    for v in vertices:
        matriz.inserirVertice(v)
    for o, d, p in arestas:
        matriz.inserirAresta(o, d, p)
    
    # GrafoLista  
    lista = GrafoLista(direcionado=True, ponderado=True)
    for v in vertices:
        lista.inserirVertice(v)
    for o, d, p in arestas:
        lista.inserirAresta(o, d, p)
    
    print("\n📊 Representação por Matriz:")
    matriz.imprimeGrafo()
    
    print("\n📋 Representação por Lista:")
    lista.imprimeGrafo()
    
    print("\n🔍 Comparação de operação existeAresta():")
    print("   (Demonstrando diferenças na implementação)")
    
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            matriz_existe = matriz.existeAresta(i, j)
            lista_existe = lista.existeAresta(i, j)
            
            if matriz_existe or lista_existe:  # Só mostra arestas que existem
                v_origem = vertices[i]
                v_destino = vertices[j]
                print(f"   {v_origem} -> {v_destino}: Matriz={matriz_existe}, Lista={lista_existe}")


def main():
    """Função principal da demonstração"""
    print("🎯 DEMONSTRAÇÃO PARTE 1 - FUNCIONALIDADES BÁSICAS DE GRAFOS")
    print("Implementação conforme slides S02 - Conceitos Básicos e Representação")
    print("Autor: Henrique Zimermann")
    print("Data: 12 de setembro de 2025")
    
    # Executar todas as demonstrações
    demonstrar_construtor()
    grafo_matriz, grafo_lista = demonstrar_vertices()
    demonstrar_arestas(grafo_matriz, grafo_lista)
    demonstrar_impressao(grafo_matriz, grafo_lista)
    demonstrar_remocao_vertices()
    demonstrar_estrutura_aresta()
    demonstrar_comparacao_representacoes()
    
    print("\n\n" + "="*80)
    print("✅ DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*80)
    print("\n📋 RESUMO DAS FUNCIONALIDADES IMPLEMENTADAS:")
    print("   ✓ Classe base Grafo com construtor direcionado/ponderado")
    print("   ✓ Especialização GrafoMatriz (matriz de adjacência)")
    print("   ✓ Especialização GrafoLista (lista de adjacência + Aresta)")
    print("   ✓ inserirVertice(label) - ambas representações")
    print("   ✓ removerVertice(indice) - ambas representações")
    print("   ✓ labelVertice(indice) - ambas representações")
    print("   ✓ imprimeGrafo() - ambas representações")
    print("   ✓ inserirAresta(origem, destino, peso) - ambas representações")
    print("   ✓ removerAresta(origem, destino) - ambas representações")
    print("   ✓ existeAresta(origem, destino) - ambas representações")
    print("   ✓ Estrutura Aresta auxiliar para GrafoLista")
    print("   ✓ Suporte completo a grafos direcionados/não direcionados")
    print("   ✓ Suporte completo a grafos ponderados/não ponderados")
    print("\n🎉 Todas as funcionalidades dos slides S02 foram implementadas!")


if __name__ == "__main__":
    main()