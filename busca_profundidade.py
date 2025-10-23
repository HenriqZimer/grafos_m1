def busca_em_profundidade(grafo, inicio: int, destino: int = None) -> list:
    visitados = [False] * len(grafo.labels)
    caminho = []

    def dfs(v):
        visitados[v] = True
        caminho.append(v)

        if destino is not None and v == destino:
            return True

        for vizinho in grafo.retornar_vizinhos(v):
            if not visitados[vizinho]:
                if dfs(vizinho):
                    return True

        return False

    dfs(inicio)
    return caminho
