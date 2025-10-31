import time

class UnionFind:
    """Estrutura Union-Find para o algoritmo de Kruskal"""
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, x, y):
        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x == raiz_y:
            return False

        if self.rank[raiz_x] < self.rank[raiz_y]:
            self.pai[raiz_x] = raiz_y
        elif self.rank[raiz_x] > self.rank[raiz_y]:
            self.pai[raiz_y] = raiz_x
        else:
            self.pai[raiz_y] = raiz_x
            self.rank[raiz_x] += 1

        return True


class MST:
    def __init__(self, grafo):
        self.grafo = grafo
        self.arestas_mst = []
        self.peso_total = 0
        self.tempo_execucao = 0

    def kruskal(self):
        """Algoritmo de Kruskal para encontrar a Árvore Geradora Mínima"""
        inicio = time.time()

        # Coletar todas as arestas do grafo
        arestas = []
        visitadas = set()
        
        for origem in range(len(self.grafo.labels)):
            for aresta in self.grafo.lista_adj[origem]:
                destino = aresta.destino
                peso = aresta.peso
                
                # Evitar adicionar a mesma aresta duas vezes em grafos não direcionados
                par = tuple(sorted([origem, destino]))
                if par not in visitadas:
                    arestas.append((peso, origem, destino))
                    visitadas.add(par)

        # Ordenar arestas por peso
        arestas.sort()

        # Aplicar Union-Find
        uf = UnionFind(len(self.grafo.labels))
        self.arestas_mst = []
        self.peso_total = 0

        for peso, origem, destino in arestas:
            if uf.union(origem, destino):
                self.arestas_mst.append((origem, destino, peso))
                self.peso_total += peso

        self.tempo_execucao = time.time() - inicio
        return self.peso_total

    def prim(self, vertice_inicial=0):
        """Algoritmo de Prim para encontrar a Árvore Geradora Mínima"""
        inicio = time.time()

        num_vertices = len(self.grafo.labels)
        visitados = [False] * num_vertices
        min_peso = [float('inf')] * num_vertices
        pai = [-1] * num_vertices

        min_peso[vertice_inicial] = 0
        self.arestas_mst = []
        self.peso_total = 0

        for _ in range(num_vertices):
            # Encontrar o vértice não visitado com menor peso
            u = -1
            for v in range(num_vertices):
                if not visitados[v] and (u == -1 or min_peso[v] < min_peso[u]):
                    u = v

            if min_peso[u] == float('inf'):
                break

            visitados[u] = True

            if pai[u] != -1:
                self.arestas_mst.append((pai[u], u, min_peso[u]))
                self.peso_total += min_peso[u]

            # Atualizar os pesos mínimos dos vizinhos
            for aresta in self.grafo.lista_adj[u]:
                v = aresta.destino
                peso = aresta.peso
                if not visitados[v] and peso < min_peso[v]:
                    min_peso[v] = peso
                    pai[v] = u

        self.tempo_execucao = time.time() - inicio
        return self.peso_total

    def imprimir_resultado(self, mostrar_arestas=False):
        print(f"Tempo de execução: {self.tempo_execucao:.6f} segundos")
        print(f"Peso total da MST: {self.peso_total}")
        print(f"Número de arestas na MST: {len(self.arestas_mst)}")

        if mostrar_arestas:
            print("\nArestas da MST:")
            for origem, destino, peso in self.arestas_mst:
                print(f"  {self.grafo.label_vertice(origem)} -- {self.grafo.label_vertice(destino)} (peso: {peso})")
