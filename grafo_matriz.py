from grafo import Grafo

class GrafoMatriz(Grafo):
    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)

        self.matriz_adj = []
        self.vertices = {}
        self.labels = []

    def inserir_vertice(self, label: str) -> bool:
        if label in self.vertices:
            return False

        self.vertices[label] = len(self.labels)
        self.labels.append(label)

        for linha in self.matriz_adj:
            linha.append(0)

        self.matriz_adj.append([0] * len(self.labels))

        return True

    def remover_vertice(self, label: str) -> bool:
        if label not in self.vertices:
            return False

        indice = self.vertices.pop(label)
        self.labels.pop(indice)

        self.matriz_adj.pop(indice)

        for linha in self.matriz_adj:
            linha.pop(indice)

        self.vertices = { label: i for i, label in enumerate(self.labels) }

        return True

    def label_vertice(self, indice: int) -> str:
        return self.labels[indice] if 0 <= indice < len(self.labels) else ""

    def inserir_aresta(self, origem: int, destino: int, peso: int = 1) -> bool:
        if origem >= len(self.labels) or destino >= len(self.labels):
            return False

        self.matriz_adj[origem][destino] = peso

        if not self.direcionado:
            self.matriz_adj[destino][origem] = peso

        return True

    def remover_aresta(self, origem: int, destino: int) -> bool:
        if origem >= len(self.labels) or destino >= len(self.labels):
            return False

        self.matriz_adj[origem][destino] = 0

        if not self.direcionado:
            self.matriz_adj[destino][origem] = 0

        return True

    def existe_aresta(self, origem: int, destino: int) -> bool:
        return self.matriz_adj[origem][destino] != 0

    def peso_aresta(self, origem: int, destino: int) -> float:
        return self.matriz_adj[origem][destino]

    def retornar_vizinhos(self, vertice: int) -> list:
        if vertice >= len(self.labels):
            return []
            
        return [i for i, peso in enumerate(self.matriz_adj[vertice]) if peso != 0]

    def imprime_grafo(self) -> None:
        for linha in self.matriz_adj:
            print(linha)
