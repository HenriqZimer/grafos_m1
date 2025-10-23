from grafo import Grafo
from aresta import Aresta

class GrafoLista(Grafo):
    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)

        self.lista_adj = {}
        self.vertices = {}
        self.labels = []

    def inserir_vertice(self, label: str) -> bool:
        if label in self.vertices:
            return False

        indice = len(self.labels)

        self.vertices[label] = indice
        self.labels.append(label)
        self.lista_adj[indice] = []

        return True

    def remover_vertice(self, label: str) -> bool:
        if label not in self.vertices:
            return False

        indice = self.vertices.pop(label)

        self.labels.pop(indice)
        self.lista_adj.pop(indice)

        for arestas in self.lista_adj.values():
            arestas[:] = [aresta for aresta in arestas if aresta.destino != indice]

        self.vertices = { label: i for i, label in enumerate(self.labels) }
        
        return True

    # def remover_vertice(self, label: str) -> bool:
    #     if label not in self.vertices:
    #         return False

    #     indice = self.vertices.pop(label)
    #     self.labels[indice] = None  # Marcar como removido

    #     # Remover arestas que referenciam este vértice
    #     for key in list(self.lista_adj.keys()):
    #         self.lista_adj[key] = [aresta for aresta in self.lista_adj[key] if aresta.destino != indice]
        
    #     return True

    def label_vertice(self, indice: int) -> str:
        return self.labels[indice] if 0 <= indice < len(self.labels) else ""

    def inserir_aresta(self, origem: int, destino: int, peso: int = 1) -> bool:
        if origem >= len(self.labels) or destino >= len(self.labels):
            return False

        self.lista_adj[origem].append(Aresta(destino, peso))

        if not self.direcionado:
            self.lista_adj[destino].append(Aresta(origem, peso))

        return True

    # def inserir_aresta(self, origem: int, destino: int, peso: int = 1) -> bool:
    #     if origem not in self.lista_adj or destino not in self.lista_adj:
    #         return False

    #     self.lista_adj[origem].append(Aresta(destino, peso))

    #     if not self.direcionado:
    #         self.lista_adj[destino].append(Aresta(origem, peso))

    #     return True

    def remover_aresta(self, origem: int, destino: int) -> bool:
        if origem >= len(self.labels) or destino >= len(self.labels):
            return False

        self.lista_adj[origem] = [aresta for aresta in self.lista_adj[origem] if aresta.destino != destino]

        if not self.direcionado:
            self.lista_adj[destino] = [aresta for aresta in self.lista_adj[destino] if aresta.destino != origem]

        return True

    def existe_aresta(self, origem: int, destino: int) -> bool:
        return any(aresta.destino == destino for aresta in self.lista_adj[origem])

    def peso_aresta(self, origem: int, destino: int) -> float:
        for aresta in self.lista_adj[origem]:
            if aresta.destino == destino:
                return aresta.peso

        return 0

    def retornar_vizinhos(self, vertice: int) -> list:
        return [aresta.destino for aresta in self.lista_adj[vertice]]

    # def retornar_vizinhos(self, vertice: int) -> list:
    #     if vertice not in self.lista_adj:
    #         return []

    #     return [aresta.destino for aresta in self.lista_adj[vertice]]

    def imprime_grafo(self) -> None:
        for vertice, arestas in self.lista_adj.items():
            print(f"{vertice}: { [f'{aresta.destino}(peso={aresta.peso})' for aresta in arestas] }")

    # def imprime_grafo(self) -> None:
    #     for vertice, arestas in self.lista_adj.items():
    #         if vertice is not None:  # Ignora vértices removidos
    #             print(f"{vertice}: { [f'{aresta.destino}(peso={aresta.peso})' for aresta in arestas] }")