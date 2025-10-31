import os
from grafo_lista import GrafoLista
from mst import MST
from coloracao_grafos import ColoracaoGrafos

def executar_testes_mst():
    """Executa testes de MST em todas as instâncias"""
    print("=" * 80)
    print("TESTES DE ÁRVORE GERADORA MÍNIMA (MST)")
    print("=" * 80)
    
    pasta_mst = "arquivos_m2/MST"
    arquivos = sorted([f for f in os.listdir(pasta_mst) if f.endswith('.txt')])
    
    resultados = []
    
    for arquivo in arquivos:
        caminho = os.path.join(pasta_mst, arquivo)
        print(f"\n{'=' * 80}")
        print(f"Arquivo: {arquivo}")
        print(f"{'=' * 80}")
        
        # Carregar grafo
        grafo = GrafoLista(direcionado=False, ponderado=True)
        grafo.ler_arquivo(caminho)
        
        print(f"Vértices: {len(grafo.labels)}")
        print(f"Arestas: {sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2}")
        
        # Kruskal
        print("\n--- Algoritmo de Kruskal ---")
        mst_kruskal = MST(grafo)
        peso_kruskal = mst_kruskal.kruskal()
        print(f"Peso total: {peso_kruskal}")
        print(f"Tempo: {mst_kruskal.tempo_execucao:.6f}s")
        
        # Prim
        print("\n--- Algoritmo de Prim ---")
        mst_prim = MST(grafo)
        peso_prim = mst_prim.prim()
        print(f"Peso total: {peso_prim}")
        print(f"Tempo: {mst_prim.tempo_execucao:.6f}s")
        
        resultados.append({
            'arquivo': arquivo,
            'vertices': len(grafo.labels),
            'arestas': sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2,
            'peso_kruskal': peso_kruskal,
            'tempo_kruskal': mst_kruskal.tempo_execucao,
            'peso_prim': peso_prim,
            'tempo_prim': mst_prim.tempo_execucao
        })
    
    return resultados


def executar_testes_coloracao():
    """Executa testes de coloração em todas as instâncias"""
    print("\n\n" + "=" * 80)
    print("TESTES DE COLORAÇÃO DE GRAFOS")
    print("=" * 80)
    
    pasta_coloracao = "arquivos_m2/coloracao"
    arquivos = sorted([f for f in os.listdir(pasta_coloracao) if f.endswith('.txt')])
    
    resultados = []
    
    for arquivo in arquivos:
        caminho = os.path.join(pasta_coloracao, arquivo)
        print(f"\n{'=' * 80}")
        print(f"Arquivo: {arquivo}")
        print(f"{'=' * 80}")
        
        # Carregar grafo
        grafo = GrafoLista(direcionado=False, ponderado=False)
        grafo.ler_arquivo(caminho)
        
        print(f"Vértices: {len(grafo.labels)}")
        print(f"Arestas: {sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2}")
        
        resultado_arquivo = {
            'arquivo': arquivo,
            'vertices': len(grafo.labels),
            'arestas': sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2
        }
        
        # Welsh-Powell
        print("\n--- Algoritmo Welsh-Powell ---")
        coloracao_wp = ColoracaoGrafos(grafo)
        cores_wp = coloracao_wp.welsh_powell()
        print(f"Número de cores: {cores_wp}")
        print(f"Tempo: {coloracao_wp.tempo_execucao:.6f}s")
        resultado_arquivo['cores_welsh_powell'] = cores_wp
        resultado_arquivo['tempo_welsh_powell'] = coloracao_wp.tempo_execucao
        
        # DSATUR
        print("\n--- Algoritmo DSATUR ---")
        coloracao_dsatur = ColoracaoGrafos(grafo)
        cores_dsatur = coloracao_dsatur.dsatur()
        print(f"Número de cores: {cores_dsatur}")
        print(f"Tempo: {coloracao_dsatur.tempo_execucao:.6f}s")
        resultado_arquivo['cores_dsatur'] = cores_dsatur
        resultado_arquivo['tempo_dsatur'] = coloracao_dsatur.tempo_execucao
        
        # Heurística Simples
        print("\n--- Heurística Simples ---")
        coloracao_simples = ColoracaoGrafos(grafo)
        cores_simples = coloracao_simples.heuristica_simples()
        print(f"Número de cores: {cores_simples}")
        print(f"Tempo: {coloracao_simples.tempo_execucao:.6f}s")
        resultado_arquivo['cores_heuristica_simples'] = cores_simples
        resultado_arquivo['tempo_heuristica_simples'] = coloracao_simples.tempo_execucao
        
        resultados.append(resultado_arquivo)
    
    return resultados


def gerar_relatorio(resultados_mst, resultados_coloracao):
    """Gera um relatório em arquivo de texto"""
    
    with open('relatorio_resultados.txt', 'w', encoding='utf-8') as f:
        f.write("=" * 100 + "\n")
        f.write(" " * 30 + "RELATÓRIO DE RESULTADOS\n")
        f.write(" " * 20 + "Trabalho de Grafos - Módulo 2\n")
        f.write("=" * 100 + "\n\n")
        
        # Relatório MST
        f.write("1. ÁRVORE GERADORA MÍNIMA (MST)\n")
        f.write("=" * 100 + "\n\n")
        
        for resultado in resultados_mst:
            f.write(f"Instância: {resultado['arquivo']}\n")
            f.write(f"  - Vértices: {resultado['vertices']}\n")
            f.write(f"  - Arestas: {resultado['arestas']}\n")
            f.write(f"\n  Algoritmo de Kruskal:\n")
            f.write(f"    • Peso total da MST: {resultado['peso_kruskal']}\n")
            f.write(f"    • Tempo de execução: {resultado['tempo_kruskal']:.6f} segundos\n")
            f.write(f"\n  Algoritmo de Prim:\n")
            f.write(f"    • Peso total da MST: {resultado['peso_prim']}\n")
            f.write(f"    • Tempo de execução: {resultado['tempo_prim']:.6f} segundos\n")
            f.write("\n" + "-" * 100 + "\n\n")
        
        # Tabela resumo MST
        f.write("\nTABELA RESUMO - MST (Kruskal)\n")
        f.write("-" * 100 + "\n")
        f.write(f"{'Instância':<40} {'Vértices':>10} {'Arestas':>10} {'Peso Total':>15} {'Tempo (s)':>12}\n")
        f.write("-" * 100 + "\n")
        for r in resultados_mst:
            f.write(f"{r['arquivo']:<40} {r['vertices']:>10} {r['arestas']:>10} "
                   f"{r['peso_kruskal']:>15} {r['tempo_kruskal']:>12.6f}\n")
        f.write("-" * 100 + "\n\n")
        
        # Relatório Coloração
        f.write("\n\n2. COLORAÇÃO DE GRAFOS\n")
        f.write("=" * 100 + "\n\n")
        
        for resultado in resultados_coloracao:
            f.write(f"Instância: {resultado['arquivo']}\n")
            f.write(f"  - Vértices: {resultado['vertices']}\n")
            f.write(f"  - Arestas: {resultado['arestas']}\n")
            f.write(f"\n  Algoritmo Welsh-Powell:\n")
            f.write(f"    • Número de cores: {resultado['cores_welsh_powell']}\n")
            f.write(f"    • Tempo de execução: {resultado['tempo_welsh_powell']:.6f} segundos\n")
            f.write(f"\n  Algoritmo DSATUR:\n")
            f.write(f"    • Número de cores: {resultado['cores_dsatur']}\n")
            f.write(f"    • Tempo de execução: {resultado['tempo_dsatur']:.6f} segundos\n")
            f.write(f"\n  Heurística Simples:\n")
            f.write(f"    • Número de cores: {resultado['cores_heuristica_simples']}\n")
            f.write(f"    • Tempo de execução: {resultado['tempo_heuristica_simples']:.6f} segundos\n")
            f.write("\n" + "-" * 100 + "\n\n")
        
        # Tabela resumo Coloração
        f.write("\nTABELA RESUMO - COLORAÇÃO\n")
        f.write("-" * 130 + "\n")
        f.write(f"{'Instância':<30} {'Vértices':>10} {'Arestas':>10} "
               f"{'Welsh-Powell':>15} {'DSATUR':>10} {'Heur. Simples':>15} {'Melhor':>10}\n")
        f.write("-" * 130 + "\n")
        for r in resultados_coloracao:
            melhor = min(r['cores_welsh_powell'], r['cores_dsatur'], r['cores_heuristica_simples'])
            f.write(f"{r['arquivo']:<30} {r['vertices']:>10} {r['arestas']:>10} "
                   f"{r['cores_welsh_powell']:>15} {r['cores_dsatur']:>10} "
                   f"{r['cores_heuristica_simples']:>15} {melhor:>10}\n")
        f.write("-" * 130 + "\n\n")
        
        # Análise comparativa
        f.write("\n\n3. ANÁLISE COMPARATIVA\n")
        f.write("=" * 100 + "\n\n")
        
        f.write("3.1. MST - Kruskal vs Prim\n")
        f.write("-" * 100 + "\n")
        for r in resultados_mst:
            if r['tempo_kruskal'] < r['tempo_prim']:
                mais_rapido = "Kruskal"
                diferenca = r['tempo_prim'] - r['tempo_kruskal']
            else:
                mais_rapido = "Prim"
                diferenca = r['tempo_kruskal'] - r['tempo_prim']
            f.write(f"{r['arquivo']:<40} Mais rápido: {mais_rapido:>8} (diferença: {diferenca:.6f}s)\n")
        
        f.write("\n\n3.2. Coloração - Comparação de Algoritmos\n")
        f.write("-" * 100 + "\n")
        for r in resultados_coloracao:
            cores = {
                'Welsh-Powell': r['cores_welsh_powell'],
                'DSATUR': r['cores_dsatur'],
                'Heurística Simples': r['cores_heuristica_simples']
            }
            melhor_alg = min(cores, key=cores.get)
            f.write(f"{r['arquivo']:<30} Melhor resultado: {melhor_alg:>20} ({cores[melhor_alg]} cores)\n")
        
        f.write("\n\n" + "=" * 100 + "\n")
        f.write("Fim do relatório\n")
        f.write("=" * 100 + "\n")
    
    print("\n\n" + "=" * 80)
    print("RELATÓRIO GERADO COM SUCESSO!")
    print(f"Arquivo: relatorio_resultados.txt")
    print("=" * 80)


if __name__ == "__main__":
    print("Iniciando execução dos testes...\n")
    
    # Executar testes
    resultados_mst = executar_testes_mst()
    resultados_coloracao = executar_testes_coloracao()
    
    # Gerar relatório
    gerar_relatorio(resultados_mst, resultados_coloracao)
    
    print("\nTodos os testes foram concluídos!")
