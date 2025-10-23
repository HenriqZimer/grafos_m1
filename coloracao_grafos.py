import time
import itertools

class ColoracaoGrafos:
    def __init__(self, grafo):
        self.grafo = grafo
        self.cores = {}
        self.tempo_execucao = 0

    def força_bruta(self):
        inicio = time.time()

        # lista de vértices
        vertices = list(range(len(self.grafo.labels)))
        
        # tenta com 2 cores até len(vertices)
        for num_cores in range(2, len(vertices) + 1):
            for combinacao in itertools.product(range(num_cores), repeat=len(vertices)):
                if self.e_coloring_valida(vertices, combinacao):
                    self.tempo_execucao = time.time() - inicio
                    self.cores = {vertices[i]: combinacao[i] for i in range(len(vertices))}

                    return num_cores

        self.tempo_execucao = time.time() - inicio

        # no pior caso, todas as cores
        return len(vertices)

    def e_coloring_valida(self, vertices, combinacao):
        for i in range(len(vertices)):
            for vizinho in self.grafo.retornar_vizinhos(i):
                # vizinhos não podem ter a mesma cor
                if combinacao[i] == combinacao[vizinho]:
                    return False

        return True

    def welsh_powell(self):
        inicio = time.time()

        vertices = list(range(len(self.grafo.labels)))
        vertices.sort(key=lambda v: len(self.grafo.retornar_vizinhos(v)), reverse=True)  # Ordena por grau decrescente
        
        num_cores = 0
        cores = [-1] * len(vertices)

        for vertice in vertices:
            # todas as cores possíveis
            cor_disponivel = set(range(len(vertices)))

            for vizinho in self.grafo.retornar_vizinhos(vertice):
                if cores[vizinho] != -1:
                    # remove cores usadas por vizinhos
                    cor_disponivel.discard(cores[vizinho])

            cores[vertice] = min(cor_disponivel)
            num_cores = max(num_cores, cores[vertice] + 1)

        self.tempo_execucao = time.time() - inicio

        self.cores = {vertices[i]: cores[i] for i in range(len(vertices))}

        return num_cores

    def dsatur(self):
        inicio = time.time()

        vertices = list(range(len(self.grafo.labels)))
        saturacao = [0] * len(vertices)
        grau = [len(self.grafo.retornar_vizinhos(v)) for v in vertices]

        cores = [-1] * len(vertices)
        num_cores = 0

        while -1 in cores:
            vertice = max(vertices, key=lambda v: (saturacao[v], grau[v]) if cores[v] == -1 else (-1, -1))
            cor_disponivel = set(range(len(vertices)))

            for vizinho in self.grafo.retornar_vizinhos(vertice):
                if cores[vizinho] != -1:
                    cor_disponivel.discard(cores[vizinho])

            cores[vertice] = min(cor_disponivel)
            num_cores = max(num_cores, cores[vertice] + 1)

            for vizinho in self.grafo.retornar_vizinhos(vertice):
                if cores[vizinho] == -1:
                    saturacao[vizinho] += 1

        self.tempo_execucao = time.time() - inicio

        self.cores = {vertices[i]: cores[i] for i in range(len(vertices))}

        return num_cores

    # heuristica gulosa 
    # o algoritmo faz escolhas locais (a menor cor disponível para cada vértice) sem seguir um critério específico de ordenação dos vértices
    def heuristica_simples(self):
        inicio = time.time()

        vertices = list(range(len(self.grafo.labels)))

        cores = [-1] * len(vertices)
        num_cores = 0

        for vertice in vertices:
            cor_disponivel = set(range(len(vertices)))

            for vizinho in self.grafo.retornar_vizinhos(vertice):
                if cores[vizinho] != -1:
                    cor_disponivel.discard(cores[vizinho])

            cores[vertice] = min(cor_disponivel)
            num_cores = max(num_cores, cores[vertice] + 1)

        self.tempo_execucao = time.time() - inicio

        self.cores = {vertices[i]: cores[i] for i in range(len(vertices))}

        return num_cores

    def imprimir_resultado(self, mostrar_cores=False):
        print(f"Tempo de execução: {self.tempo_execucao:.6f} segundos")
        print(f"Número de cores usadas: {len(set(self.cores.values()))}")

        if mostrar_cores:
            for vertice, cor in self.cores.items():
                print(f"Vértice {self.grafo.label_vertice(vertice)} - Cor {cor}")
