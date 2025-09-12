"""
Trabalho M1 - Parte 2: Algoritmos de Busca e Leitura de Arquivos
Extensão da implementação de grafos com BFS, DFS, Dijkstra e leitura de arquivos
Autor: Henrique Zimermann
Data: 11 de setembro de 2025
"""

from collections import deque
import heapq
import math

class Grafo:
    """
    Classe que implementa um grafo com duas representações:
    - Lista de adjacência
    - Matriz de adjacência
    
    PARTE 2: Inclui algoritmos de busca e leitura de arquivos
    """
    
    def __init__(self, num_vertices=0, dirigido=False, arquivo=None):
        """
        Inicializa o grafo
        
        Args:
            num_vertices (int): Número de vértices do grafo
            dirigido (bool): Se o grafo é dirigido ou não
            arquivo (str): Caminho para arquivo de grafo (opcional)
        """
        if arquivo:
            self._carregar_de_arquivo(arquivo)
        else:
            self.num_vertices = num_vertices
            self.dirigido = dirigido
            self.ponderado = False
            
            # Representação por lista de adjacência
            self.lista_adjacencia = [[] for _ in range(num_vertices)]
            
            # Representação por matriz de adjacência
            self.matriz_adjacencia = [[0 for _ in range(num_vertices)] 
                                     for _ in range(num_vertices)]
    
    def _carregar_de_arquivo(self, caminho_arquivo):
        """
        Carrega o grafo a partir de um arquivo no formato especificado
        
        Formato:
        V A D P
        Ao Ad Ap (A linhas)
        
        Args:
            caminho_arquivo (str): Caminho para o arquivo
        """
        try:
            with open(caminho_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
                
                # Primeira linha: V A D P
                primeira_linha = linhas[0].strip().split()
                self.num_vertices = int(primeira_linha[0])
                num_arestas = int(primeira_linha[1])
                self.dirigido = bool(int(primeira_linha[2]))
                self.ponderado = bool(int(primeira_linha[3]))
                
                # Inicializar estruturas
                self.lista_adjacencia = [[] for _ in range(self.num_vertices)]
                self.matriz_adjacencia = [[0 for _ in range(self.num_vertices)] 
                                         for _ in range(self.num_vertices)]
                
                # Ler arestas
                for i in range(1, num_arestas + 1):
                    partes = linhas[i].strip().split()
                    origem = int(partes[0])
                    destino = int(partes[1])
                    
                    if self.ponderado:
                        peso = float(partes[2]) if len(partes) > 2 else 1.0
                    else:
                        peso = 1
                    
                    self._adicionar_aresta_interna(origem, destino, peso)
                    
                print(f"Grafo carregado: {self.num_vertices} vértices, {num_arestas} arestas")
                print(f"Dirigido: {self.dirigido}, Ponderado: {self.ponderado}")
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo '{caminho_arquivo}' não encontrado")
        except Exception as e:
            raise Exception(f"Erro ao carregar arquivo: {e}")
    
    def salvar_em_arquivo(self, caminho_arquivo):
        """
        Salva o grafo em um arquivo no formato especificado
        
        Args:
            caminho_arquivo (str): Caminho para salvar o arquivo
        """
        try:
            with open(caminho_arquivo, 'w') as arquivo:
                # Primeira linha: V A D P
                num_arestas = self.obter_num_arestas()
                arquivo.write(f"{self.num_vertices} {num_arestas} ")
                arquivo.write(f"{1 if self.dirigido else 0} ")
                arquivo.write(f"{1 if self.ponderado else 0}\n")
                
                # Arestas
                arestas_escritas = set()
                for i in range(self.num_vertices):
                    for j, peso in self.lista_adjacencia[i]:
                        if self.dirigido or (i, j) not in arestas_escritas:
                            if self.ponderado:
                                arquivo.write(f"{i} {j} {peso}\n")
                            else:
                                arquivo.write(f"{i} {j}\n")
                            
                            if not self.dirigido:
                                arestas_escritas.add((j, i))
                
                print(f"Grafo salvo em '{caminho_arquivo}'")
                
        except Exception as e:
            raise Exception(f"Erro ao salvar arquivo: {e}")
    
    def _adicionar_aresta_interna(self, origem, destino, peso=1):
        """
        Adiciona uma aresta internamente (usado na leitura de arquivo)
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            peso (float): Peso da aresta
        """
        # Adiciona na lista de adjacência
        if destino not in [v for v, p in self.lista_adjacencia[origem]]:
            self.lista_adjacencia[origem].append((destino, peso))
        
        # Adiciona na matriz de adjacência
        self.matriz_adjacencia[origem][destino] = peso
        
        # Se não é dirigido, adiciona a aresta reversa
        if not self.dirigido:
            if origem not in [v for v, p in self.lista_adjacencia[destino]]:
                self.lista_adjacencia[destino].append((origem, peso))
            self.matriz_adjacencia[destino][origem] = peso
    
    def adicionar_aresta(self, origem, destino, peso=1):
        """
        Adiciona uma aresta ao grafo
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            peso (float): Peso da aresta (default=1)
        """
        if not self._vertice_valido(origem) or not self._vertice_valido(destino):
            raise ValueError("Vértice inválido")
        
        self._adicionar_aresta_interna(origem, destino, peso)
        
        if peso != 1:
            self.ponderado = True
    
    def remover_aresta(self, origem, destino):
        """
        Remove uma aresta do grafo
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
        """
        if not self._vertice_valido(origem) or not self._vertice_valido(destino):
            raise ValueError("Vértice inválido")
        
        # Remove da lista de adjacência
        self.lista_adjacencia[origem] = [(v, p) for v, p in self.lista_adjacencia[origem] 
                                        if v != destino]
        
        # Remove da matriz de adjacência
        self.matriz_adjacencia[origem][destino] = 0
        
        # Se não é dirigido, remove a aresta reversa
        if not self.dirigido:
            self.lista_adjacencia[destino] = [(v, p) for v, p in self.lista_adjacencia[destino] 
                                             if v != origem]
            self.matriz_adjacencia[destino][origem] = 0
    
    def busca_largura(self, origem):
        """
        Busca em Largura (BFS) a partir de um vértice de origem
        
        Args:
            origem (int): Vértice de origem
            
        Returns:
            list: Lista com a ordem de visitação dos vértices
        """
        if not self._vertice_valido(origem):
            raise ValueError("Vértice de origem inválido")
        
        visitados = [False] * self.num_vertices
        ordem_visitacao = []
        fila = deque([origem])
        visitados[origem] = True
        
        print(f"\n=== Busca em Largura (BFS) a partir do vértice {origem} ===")
        
        while fila:
            vertice_atual = fila.popleft()
            ordem_visitacao.append(vertice_atual)
            print(f"Visitando vértice: {vertice_atual}")
            
            # Visitar vizinhos em ordem crescente
            vizinhos = sorted([v for v, _ in self.lista_adjacencia[vertice_atual]])
            
            for vizinho in vizinhos:
                if not visitados[vizinho]:
                    visitados[vizinho] = True
                    fila.append(vizinho)
                    print(f"  Adicionando vértice {vizinho} à fila")
        
        vertices_nao_alcancaveis = [i for i in range(self.num_vertices) if not visitados[i]]
        if vertices_nao_alcancaveis:
            print(f"Vértices não alcançáveis: {vertices_nao_alcancaveis}")
        
        print(f"Ordem de visitação: {ordem_visitacao}")
        return ordem_visitacao
    
    def busca_profundidade(self, origem):
        """
        Busca em Profundidade (DFS) a partir de um vértice de origem
        
        Args:
            origem (int): Vértice de origem
            
        Returns:
            list: Lista com a ordem de visitação dos vértices
        """
        if not self._vertice_valido(origem):
            raise ValueError("Vértice de origem inválido")
        
        visitados = [False] * self.num_vertices
        ordem_visitacao = []
        
        print(f"\n=== Busca em Profundidade (DFS) a partir do vértice {origem} ===")
        
        def dfs_recursivo(vertice):
            visitados[vertice] = True
            ordem_visitacao.append(vertice)
            print(f"Visitando vértice: {vertice}")
            
            # Visitar vizinhos em ordem crescente
            vizinhos = sorted([v for v, _ in self.lista_adjacencia[vertice]])
            
            for vizinho in vizinhos:
                if not visitados[vizinho]:
                    print(f"  Explorando vértice {vizinho}")
                    dfs_recursivo(vizinho)
        
        dfs_recursivo(origem)
        
        vertices_nao_alcancaveis = [i for i in range(self.num_vertices) if not visitados[i]]
        if vertices_nao_alcancaveis:
            print(f"Vértices não alcançáveis: {vertices_nao_alcancaveis}")
        
        print(f"Ordem de visitação: {ordem_visitacao}")
        return ordem_visitacao
    
    def dijkstra(self, origem):
        """
        Algoritmo de Dijkstra para encontrar caminhos mínimos
        
        Args:
            origem (int): Vértice de origem
            
        Returns:
            tuple: (distancias, predecessores) onde:
                   distancias[i] = menor distância de origem até i
                   predecessores[i] = predecessor de i no caminho mínimo
        """
        if not self._vertice_valido(origem):
            raise ValueError("Vértice de origem inválido")
        
        if not self.ponderado:
            print("AVISO: Aplicando Dijkstra em grafo não ponderado (pesos = 1)")
        
        # Inicialização
        distancias = [math.inf] * self.num_vertices
        predecessores = [-1] * self.num_vertices
        visitados = [False] * self.num_vertices
        
        distancias[origem] = 0
        
        # Heap de prioridade: (distância, vértice)
        heap = [(0, origem)]
        
        print(f"\n=== Algoritmo de Dijkstra a partir do vértice {origem} ===")
        print(f"Inicialização: distância[{origem}] = 0")
        
        while heap:
            dist_atual, u = heapq.heappop(heap)
            
            # Se já foi visitado, continue
            if visitados[u]:
                continue
            
            visitados[u] = True
            print(f"\nProcessando vértice {u} (distância: {dist_atual})")
            
            # Relaxar arestas adjacentes
            for v, peso in self.lista_adjacencia[u]:
                if not visitados[v]:
                    nova_distancia = distancias[u] + peso
                    
                    if nova_distancia < distancias[v]:
                        distancias[v] = nova_distancia
                        predecessores[v] = u
                        heapq.heappush(heap, (nova_distancia, v))
                        
                        print(f"  Atualizando distância[{v}]: {nova_distancia} "
                              f"(predecessor: {u})")
        
        # Imprimir resultados
        print(f"\n=== Resultados do Dijkstra ===")
        print(f"Vértice de origem: {origem}")
        print(f"{'Destino':<8} {'Distância':<12} {'Caminho'}")
        print("-" * 35)
        
        for destino in range(self.num_vertices):
            if distancias[destino] == math.inf:
                print(f"{destino:<8} {'∞':<12} Não alcançável")
            else:
                caminho = self._reconstruir_caminho(origem, destino, predecessores)
                caminho_str = " → ".join(map(str, caminho))
                print(f"{destino:<8} {distancias[destino]:<12.1f} {caminho_str}")
        
        return distancias, predecessores
    
    def _reconstruir_caminho(self, origem, destino, predecessores):
        """
        Reconstrói o caminho do vértice origem até o destino
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            predecessores (list): Lista de predecessores do Dijkstra
            
        Returns:
            list: Caminho do origem até destino
        """
        if predecessores[destino] == -1 and origem != destino:
            return []  # Não há caminho
        
        caminho = []
        atual = destino
        
        while atual != -1:
            caminho.append(atual)
            atual = predecessores[atual]
        
        caminho.reverse()
        return caminho
    
    # ===============================
    # MÉTODOS DA PARTE 1
    # ===============================
    
    def existe_aresta(self, origem, destino):
        """Verifica se existe uma aresta entre dois vértices"""
        if not self._vertice_valido(origem) or not self._vertice_valido(destino):
            return False
        return self.matriz_adjacencia[origem][destino] != 0
    
    def obter_vizinhos(self, vertice):
        """Obtém os vizinhos de um vértice"""
        if not self._vertice_valido(vertice):
            return []
        return self.lista_adjacencia[vertice].copy()
    
    def obter_grau(self, vertice):
        """Obtém o grau de um vértice"""
        if not self._vertice_valido(vertice):
            return 0
        return len(self.lista_adjacencia[vertice])
    
    def obter_grau_entrada(self, vertice):
        """Obtém o grau de entrada de um vértice (apenas para grafos dirigidos)"""
        if not self._vertice_valido(vertice):
            return 0
        
        grau_entrada = 0
        for i in range(self.num_vertices):
            if self.matriz_adjacencia[i][vertice] != 0:
                grau_entrada += 1
        return grau_entrada
    
    def obter_grau_saida(self, vertice):
        """Obtém o grau de saída de um vértice"""
        return self.obter_grau(vertice)
    
    def obter_num_arestas(self):
        """Obtém o número total de arestas do grafo"""
        num_arestas = 0
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    num_arestas += 1
        
        if not self.dirigido:
            num_arestas //= 2
        return num_arestas
    
    def obter_vertices(self):
        """Obtém a lista de todos os vértices"""
        return list(range(self.num_vertices))
    
    def obter_arestas(self):
        """Obtém a lista de todas as arestas"""
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    if self.dirigido or i <= j:
                        arestas.append((i, j, self.matriz_adjacencia[i][j]))
        return arestas
    
    def eh_conexo(self):
        """Verifica se o grafo é conexo (para grafos não dirigidos)"""
        if self.dirigido:
            return False
        
        if self.num_vertices == 0:
            return True
        
        visitados = [False] * self.num_vertices
        self._dfs_conexo(0, visitados)
        return all(visitados)
    
    def densidade(self):
        """Calcula a densidade do grafo"""
        if self.num_vertices <= 1:
            return 0.0
        
        num_arestas = self.obter_num_arestas()
        if self.dirigido:
            max_arestas = self.num_vertices * (self.num_vertices - 1)
        else:
            max_arestas = self.num_vertices * (self.num_vertices - 1) // 2
        
        return num_arestas / max_arestas if max_arestas > 0 else 0.0
    
    def _dfs_conexo(self, vertice, visitados):
        """Busca em profundidade auxiliar para verificar conectividade"""
        visitados[vertice] = True
        for vizinho, _ in self.lista_adjacencia[vertice]:
            if not visitados[vizinho]:
                self._dfs_conexo(vizinho, visitados)
    
    def _vertice_valido(self, vertice):
        """Verifica se um vértice é válido"""
        return 0 <= vertice < self.num_vertices
    
    def imprimir_lista_adjacencia(self):
        """Imprime a representação por lista de adjacência"""
        print("Lista de Adjacência:")
        for i in range(self.num_vertices):
            vizinhos = [f"{v}({p})" for v, p in self.lista_adjacencia[i]]
            print(f"Vértice {i}: {vizinhos}")
    
    def imprimir_matriz_adjacencia(self):
        """Imprime a representação por matriz de adjacência"""
        print("Matriz de Adjacência:")
        print("   ", end="")
        for j in range(self.num_vertices):
            print(f"{j:6}", end="")
        print()
        
        for i in range(self.num_vertices):
            print(f"{i:2}:", end="")
            for j in range(self.num_vertices):
                print(f"{self.matriz_adjacencia[i][j]:6.1f}", end="")
            print()
    
    def __str__(self):
        """Representação em string do grafo"""
        tipo = "Dirigido" if self.dirigido else "Não dirigido"
        ponderado = "Ponderado" if self.ponderado else "Não ponderado"
        return (f"Grafo {tipo}, {ponderado} com {self.num_vertices} vértices "
                f"e {self.obter_num_arestas()} arestas")


def main():
    """Função principal para testar a implementação da Parte 2"""
    print("=== Teste da implementação de Grafo - PARTE 2 ===\n")
    
    # Teste 1: Criar e salvar um grafo de exemplo
    print("1. Criando grafo de exemplo:")
    grafo = Grafo(6, dirigido=False)
    grafo.ponderado = True
    
    # Criando um grafo interessante para testar os algoritmos
    arestas = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10),
        (3, 4, 2), (3, 5, 6),
        (4, 5, 3)
    ]
    
    for origem, destino, peso in arestas:
        grafo.adicionar_aresta(origem, destino, peso)
    
    print(grafo)
    grafo.imprimir_lista_adjacencia()
    print()
    
    # Salvar em arquivo
    grafo.salvar_em_arquivo("grafo_exemplo.txt")
    print()
    
    # Teste 2: Carregar grafo do arquivo
    print("2. Carregando grafo do arquivo:")
    grafo_carregado = Grafo(arquivo="grafo_exemplo.txt")
    print(grafo_carregado)
    print()
    
    # Teste 3: Busca em Largura
    print("3. Testando Busca em Largura:")
    ordem_bfs = grafo_carregado.busca_largura(0)
    print()
    
    # Teste 4: Busca em Profundidade
    print("4. Testando Busca em Profundidade:")
    ordem_dfs = grafo_carregado.busca_profundidade(0)
    print()
    
    # Teste 5: Algoritmo de Dijkstra
    print("5. Testando Algoritmo de Dijkstra:")
    distancias, predecessores = grafo_carregado.dijkstra(0)
    print()
    
    print("=== Testes da Parte 2 concluídos! ===")

if __name__ == "__main__":
    main()