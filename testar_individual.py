"""
Script para testar algoritmos individualmente
"""

from grafo_lista import GrafoLista
from mst import MST
from coloracao_grafos import ColoracaoGrafos

def testar_mst(arquivo):
    """Testa algoritmos de MST em um arquivo específico"""
    print(f"\n{'=' * 80}")
    print(f"TESTE DE MST: {arquivo}")
    print(f"{'=' * 80}\n")
    
    grafo = GrafoLista(direcionado=False, ponderado=True)
    grafo.ler_arquivo(arquivo)
    
    print(f"Vértices: {len(grafo.labels)}")
    print(f"Arestas: {sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2}\n")
    
    # Kruskal
    print("--- Algoritmo de Kruskal ---")
    mst_kruskal = MST(grafo)
    peso = mst_kruskal.kruskal()
    mst_kruskal.imprimir_resultado(mostrar_arestas=False)
    
    # Prim
    print("\n--- Algoritmo de Prim ---")
    mst_prim = MST(grafo)
    peso = mst_prim.prim()
    mst_prim.imprimir_resultado(mostrar_arestas=False)


def testar_coloracao(arquivo):
    """Testa algoritmos de coloração em um arquivo específico"""
    print(f"\n{'=' * 80}")
    print(f"TESTE DE COLORAÇÃO: {arquivo}")
    print(f"{'=' * 80}\n")
    
    grafo = GrafoLista(direcionado=False, ponderado=False)
    grafo.ler_arquivo(arquivo)
    
    print(f"Vértices: {len(grafo.labels)}")
    print(f"Arestas: {sum(len(grafo.lista_adj[v]) for v in grafo.lista_adj) // 2}\n")
    
    # Welsh-Powell
    print("--- Algoritmo Welsh-Powell ---")
    coloracao_wp = ColoracaoGrafos(grafo)
    cores = coloracao_wp.welsh_powell()
    coloracao_wp.imprimir_resultado(mostrar_cores=False)
    
    # DSATUR
    print("\n--- Algoritmo DSATUR ---")
    coloracao_dsatur = ColoracaoGrafos(grafo)
    cores = coloracao_dsatur.dsatur()
    coloracao_dsatur.imprimir_resultado(mostrar_cores=False)
    
    # Heurística Simples
    print("\n--- Heurística Simples ---")
    coloracao_simples = ColoracaoGrafos(grafo)
    cores = coloracao_simples.heuristica_simples()
    coloracao_simples.imprimir_resultado(mostrar_cores=False)


def menu():
    """Menu interativo"""
    while True:
        print("\n" + "=" * 80)
        print("MENU DE TESTES")
        print("=" * 80)
        print("1. Testar MST")
        print("2. Testar Coloração")
        print("3. Sair")
        print("=" * 80)
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            print("\nArquivos disponíveis para MST:")
            print("  1. 50vertices25%Arestas.txt")
            print("  2. 50vertices50%Arestas.txt")
            print("  3. 50vertices100%Arestas.txt")
            print("  4. 500vertices25%Arestas.txt")
            print("  5. 500vertices50%Arestas.txt")
            print("  6. 500vertices100%Arestas.txt")
            print("  7. 1000vertices25%Arestas.txt")
            print("  8. Outro arquivo (digite o caminho)")
            
            escolha = input("\nEscolha o arquivo: ").strip()
            
            arquivos_mst = {
                "1": "arquivos_m2/MST/50vertices25%Arestas.txt",
                "2": "arquivos_m2/MST/50vertices50%Arestas.txt",
                "3": "arquivos_m2/MST/50vertices100%Arestas.txt",
                "4": "arquivos_m2/MST/500vertices25%Arestas.txt",
                "5": "arquivos_m2/MST/500vertices50%Arestas.txt",
                "6": "arquivos_m2/MST/500vertices100%Arestas.txt",
                "7": "arquivos_m2/MST/1000vertices25%Arestas.txt"
            }
            
            if escolha in arquivos_mst:
                testar_mst(arquivos_mst[escolha])
            elif escolha == "8":
                caminho = input("Digite o caminho do arquivo: ").strip()
                testar_mst(caminho)
            else:
                print("Opção inválida!")
                
        elif opcao == "2":
            print("\nArquivos disponíveis para Coloração:")
            print("  1. k33.txt")
            print("  2. k5.txt")
            print("  3. kquase5.txt")
            print("  4. r250-66-65.txt")
            print("  5. r1000-234-234.txt")
            print("  6. C4000-260-X.txt")
            print("  7. Outro arquivo (digite o caminho)")
            
            escolha = input("\nEscolha o arquivo: ").strip()
            
            arquivos_coloracao = {
                "1": "arquivos_m2/coloracao/k33.txt",
                "2": "arquivos_m2/coloracao/k5.txt",
                "3": "arquivos_m2/coloracao/kquase5.txt",
                "4": "arquivos_m2/coloracao/r250-66-65.txt",
                "5": "arquivos_m2/coloracao/r1000-234-234.txt",
                "6": "arquivos_m2/coloracao/C4000-260-X.txt"
            }
            
            if escolha in arquivos_coloracao:
                testar_coloracao(arquivos_coloracao[escolha])
            elif escolha == "7":
                caminho = input("Digite o caminho do arquivo: ").strip()
                testar_coloracao(caminho)
            else:
                print("Opção inválida!")
                
        elif opcao == "3":
            print("\nEncerrando...")
            break
        else:
            print("\nOpção inválida!")


if __name__ == "__main__":
    print("=" * 80)
    print("TESTE INTERATIVO DE ALGORITMOS DE GRAFOS")
    print("=" * 80)
    menu()
