def dijkstra(grafo, inicio: int):
    num_vertices = len(grafo.labels)
    distancias = [float('inf')] * num_vertices
    anteriores = [None] * num_vertices
    distancias[inicio] = 0
    visitados = [False] * num_vertices

    for _ in range(num_vertices):
        menor_distancia = float('inf')
        vertice_atual = None

        for vertice in range(num_vertices):
            if not visitados[vertice] and distancias[vertice] < menor_distancia:
                menor_distancia = distancias[vertice]
                vertice_atual = vertice

        if vertice_atual is None:  
            break

        visitados[vertice_atual] = True

        for vizinho in grafo.retornar_vizinhos(vertice_atual):
            peso = grafo.peso_aresta(vertice_atual, vizinho)
            distancia = distancias[vertice_atual] + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                anteriores[vizinho] = vertice_atual

    caminhos = []
    for destino in range(num_vertices):
        if distancias[destino] == float('inf'):
            caminhos.append((destino, "Inacessível", []))
            continue

        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = anteriores[atual]
        caminhos.append((destino, distancias[destino], list(reversed(caminho))))

    return distancias, caminhos

def print_dijkstra(distancias, caminhos):
    for destino, distancia, caminho in caminhos:
        if distancia == "Inacessível":
            print(f"Vértice {destino}: Inacessível")
        else:
            caminho_str = " -> ".join(map(str, caminho))
            print(f"Vértice {destino}:")
            print(f"  Distância: {distancia}")
            print(f"  Caminho: {caminho_str}\n")
