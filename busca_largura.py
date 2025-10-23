from collections import deque

def busca_em_largura(grafo, inicio: int, destino: int = None) -> list:
    visitados = [False] * len(grafo.labels)
    caminho = []
    fila = deque([inicio])
    visitados[inicio] = True
    
    while fila:
        vertice = fila.popleft()
        caminho.append(vertice)

        if destino is not None and vertice == destino:
            return caminho
        
        vizinhos = grafo.retornar_vizinhos(vertice)
        for vizinho in vizinhos:
            if not visitados[vizinho]:
                fila.append(vizinho)
                visitados[vizinho] = True

    return caminho  
