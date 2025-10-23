# from grafo_matriz import GrafoMatriz
# from grafo_lista import GrafoLista
# from busca_largura import busca_em_largura
# from busca_profundidade import busca_em_profundidade
# from dijkstra import dijkstra, print_dijkstra

# def testar_grafo_lista():
#     print("Testando Grafo com Lista de Adjacência")
#     grafo = GrafoLista(direcionado=False, ponderado=True)
#     grafo.ler_arquivo("test.txt")
#     grafo.imprime_grafo()


#     print("\nBusca em Largura (Sem destino):")
#     resultado_largura = busca_em_largura(grafo, 0)
#     print(f"Ordem de visita: {resultado_largura}")

#     print("\nBusca em Largura (Com destino):")
#     caminho_largura = busca_em_largura(grafo, 0, 3)
#     print(f"Caminho até o vértice 3: {caminho_largura}")

#     print("\nBusca em Profundidade (Sem destino):")
#     resultado_profundidade = busca_em_profundidade(grafo, 0)
#     print(f"Ordem de visita: {resultado_profundidade}")

#     print("\nBusca em Profundidade (Com destino):")
#     caminho_profundidade = busca_em_profundidade(grafo, 0, 3)
#     print(f"Caminho até o vértice 3: {caminho_profundidade}")

#     print("\nDijkstra:")
#     distancias, caminhos = dijkstra(grafo, 0)
#     print_dijkstra(distancias, caminhos)

# def testar_grafo_matriz():
#     print("Testando Grafo com Matriz de Adjacência")
#     grafo = GrafoMatriz(direcionado=False, ponderado=True)
#     grafo.ler_arquivo("test.txt")
#     grafo.imprime_grafo()

#     print("\nBusca em Largura:")
#     resultado_largura = busca_em_largura(grafo, 0)
#     print(f"Ordem de visita: {resultado_largura}")

#     print("\nBusca em Profundidade:")
#     resultado_profundidade = busca_em_profundidade(grafo, 0)
#     print(f"Ordem de visita: {resultado_profundidade}")

#     print("\nDijkstra:")
#     distancias, caminhos = dijkstra(grafo, 0)
#     print_dijkstra(distancias, caminhos)

# if __name__ == "__main__":
#     testar_grafo_lista()
#     testar_grafo_matriz()

from grafo_lista import GrafoLista
from grafo_matriz import GrafoMatriz
from coloracao_grafos import ColoracaoGrafos

def main():
    grafo = GrafoLista(direcionado=False, ponderado=False)
    grafo.ler_arquivo('grafo.txt')

    coloracao = ColoracaoGrafos(grafo)

    # print("Teste Força Bruta")
    # num_cores = coloracao.força_bruta()
    # coloracao.imprimir_resultado(mostrar_cores=True)

    print("\nTeste Welsh Powell")
    num_cores = coloracao.welsh_powell()
    coloracao.imprimir_resultado(mostrar_cores=True)

    print("\nTeste DSATUR")
    num_cores = coloracao.dsatur()
    coloracao.imprimir_resultado(mostrar_cores=True)

    print("\nTeste Heurística Simples")
    num_cores = coloracao.heuristica_simples()
    coloracao.imprimir_resultado(mostrar_cores=True)

if __name__ == "__main__":
    main()