"""
Trabalho M1 - Parte 1: Implementação de Grafos
Implementação de grafo com representações por lista e matriz de adjacência
Autor: Henrique Zimermann
Data: 11 de setembro de 2025
"""

class Grafo:
    """
    Classe que implementa um grafo com duas representações:
    - Lista de adjacência
    - Matriz de adjacência
    """
    
    def __init__(self, num_vertices, dirigido=False):
        """
        Inicializa o grafo
        
        Args:
            num_vertices (int): Número de vértices do grafo
            dirigido (bool): Se o grafo é dirigido ou não
        """
        self.num_vertices = num_vertices
        self.dirigido = dirigido
        
        # Representação por lista de adjacência
        self.lista_adjacencia = [[] for _ in range(num_vertices)]
        
        # Representação por matriz de adjacência
        self.matriz_adjacencia = [[0 for _ in range(num_vertices)] 
                                 for _ in range(num_vertices)]
    
    def adicionar_aresta(self, origem, destino, peso=1):
        """
        Adiciona uma aresta ao grafo
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            peso (int): Peso da aresta (default=1)
        """
        if not self._vertice_valido(origem) or not self._vertice_valido(destino):
            raise ValueError("Vértice inválido")
        
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
    
    def existe_aresta(self, origem, destino):
        """
        Verifica se existe uma aresta entre dois vértices
        
        Args:
            origem (int): Vértice de origem
            destino (int): Vértice de destino
            
        Returns:
            bool: True se existe a aresta, False caso contrário
        """
        if not self._vertice_valido(origem) or not self._vertice_valido(destino):
            return False
        
        return self.matriz_adjacencia[origem][destino] != 0
    
    def obter_vizinhos(self, vertice):
        """
        Obtém os vizinhos de um vértice
        
        Args:
            vertice (int): Vértice
            
        Returns:
            list: Lista de vizinhos (vértice, peso)
        """
        if not self._vertice_valido(vertice):
            return []
        
        return self.lista_adjacencia[vertice].copy()
    
    def obter_grau(self, vertice):
        """
        Obtém o grau de um vértice
        
        Args:
            vertice (int): Vértice
            
        Returns:
            int: Grau do vértice
        """
        if not self._vertice_valido(vertice):
            return 0
        
        if self.dirigido:
            # Para grafo dirigido, retorna grau de saída
            return len(self.lista_adjacencia[vertice])
        else:
            # Para grafo não dirigido
            return len(self.lista_adjacencia[vertice])
    
    def obter_grau_entrada(self, vertice):
        """
        Obtém o grau de entrada de um vértice (apenas para grafos dirigidos)
        
        Args:
            vertice (int): Vértice
            
        Returns:
            int: Grau de entrada do vértice
        """
        if not self._vertice_valido(vertice):
            return 0
        
        grau_entrada = 0
        for i in range(self.num_vertices):
            if self.matriz_adjacencia[i][vertice] != 0:
                grau_entrada += 1
        
        return grau_entrada
    
    def obter_grau_saida(self, vertice):
        """
        Obtém o grau de saída de um vértice
        
        Args:
            vertice (int): Vértice
            
        Returns:
            int: Grau de saída do vértice
        """
        return self.obter_grau(vertice)
    
    def obter_num_arestas(self):
        """
        Obtém o número total de arestas do grafo
        
        Returns:
            int: Número de arestas
        """
        num_arestas = 0
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    num_arestas += 1
        
        # Se não é dirigido, cada aresta foi contada duas vezes
        if not self.dirigido:
            num_arestas //= 2
        
        return num_arestas
    
    def obter_vertices(self):
        """
        Obtém a lista de todos os vértices
        
        Returns:
            list: Lista de vértices (0 a num_vertices-1)
        """
        return list(range(self.num_vertices))
    
    def obter_arestas(self):
        """
        Obtém a lista de todas as arestas
        
        Returns:
            list: Lista de tuplas (origem, destino, peso)
        """
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.matriz_adjacencia[i][j] != 0:
                    if self.dirigido or i <= j:  # Evita duplicatas em grafos não dirigidos
                        arestas.append((i, j, self.matriz_adjacencia[i][j]))
        
        return arestas
    
    def eh_conexo(self):
        """
        Verifica se o grafo é conexo (para grafos não dirigidos)
        
        Returns:
            bool: True se o grafo é conexo, False caso contrário
        """
        if self.dirigido:
            return False  # Implementação para grafos dirigidos seria mais complexa
        
        if self.num_vertices == 0:
            return True
        
        # DFS a partir do vértice 0
        visitados = [False] * self.num_vertices
        self._dfs(0, visitados)
        
        # Verifica se todos os vértices foram visitados
        return all(visitados)
    
    def _dfs(self, vertice, visitados):
        """
        Busca em profundidade auxiliar
        
        Args:
            vertice (int): Vértice atual
            visitados (list): Lista de vértices visitados
        """
        visitados[vertice] = True
        
        for vizinho, _ in self.lista_adjacencia[vertice]:
            if not visitados[vizinho]:
                self._dfs(vizinho, visitados)
    
    def _vertice_valido(self, vertice):
        """
        Verifica se um vértice é válido
        
        Args:
            vertice (int): Vértice
            
        Returns:
            bool: True se o vértice é válido, False caso contrário
        """
        return 0 <= vertice < self.num_vertices
    
    def imprimir_lista_adjacencia(self):
        """
        Imprime a representação por lista de adjacência
        """
        print("Lista de Adjacência:")
        for i in range(self.num_vertices):
            vizinhos = [f"{v}({p})" for v, p in self.lista_adjacencia[i]]
            print(f"Vértice {i}: {vizinhos}")
    
    def imprimir_matriz_adjacencia(self):
        """
        Imprime a representação por matriz de adjacência
        """
        print("Matriz de Adjacência:")
        print("   ", end="")
        for j in range(self.num_vertices):
            print(f"{j:3}", end="")
        print()
        
        for i in range(self.num_vertices):
            print(f"{i:2}:", end="")
            for j in range(self.num_vertices):
                print(f"{self.matriz_adjacencia[i][j]:3}", end="")
            print()
    
    def __str__(self):
        """
        Representação em string do grafo
        
        Returns:
            str: Descrição do grafo
        """
        tipo = "Dirigido" if self.dirigido else "Não dirigido"
        return (f"Grafo {tipo} com {self.num_vertices} vértices "
                f"e {self.obter_num_arestas()} arestas")


def main():
    """
    Função principal para testar a implementação
    """
    print("=== Teste da implementação de Grafo ===\n")
    
    # Teste 1: Grafo não dirigido
    print("1. Testando grafo não dirigido:")
    grafo1 = Grafo(5, dirigido=False)
    
    # Adicionando arestas
    grafo1.adicionar_aresta(0, 1, 2)
    grafo1.adicionar_aresta(0, 4, 1)
    grafo1.adicionar_aresta(1, 2, 3)
    grafo1.adicionar_aresta(1, 3, 4)
    grafo1.adicionar_aresta(2, 3, 1)
    grafo1.adicionar_aresta(3, 4, 2)
    
    print(grafo1)
    print()
    
    grafo1.imprimir_lista_adjacencia()
    print()
    
    grafo1.imprimir_matriz_adjacencia()
    print()
    
    # Testando funções básicas
    print("Funções básicas:")
    print(f"Existe aresta (0,1): {grafo1.existe_aresta(0, 1)}")
    print(f"Existe aresta (0,2): {grafo1.existe_aresta(0, 2)}")
    print(f"Vizinhos do vértice 1: {grafo1.obter_vizinhos(1)}")
    print(f"Grau do vértice 1: {grafo1.obter_grau(1)}")
    print(f"Número total de arestas: {grafo1.obter_num_arestas()}")
    print(f"Grafo é conexo: {grafo1.eh_conexo()}")
    print()
    
    # Teste 2: Grafo dirigido
    print("2. Testando grafo dirigido:")
    grafo2 = Grafo(4, dirigido=True)
    
    grafo2.adicionar_aresta(0, 1, 1)
    grafo2.adicionar_aresta(0, 2, 1)
    grafo2.adicionar_aresta(1, 2, 1)
    grafo2.adicionar_aresta(2, 3, 1)
    
    print(grafo2)
    print()
    
    grafo2.imprimir_lista_adjacencia()
    print()
    
    grafo2.imprimir_matriz_adjacencia()
    print()
    
    print("Graus (grafo dirigido):")
    for v in range(grafo2.num_vertices):
        print(f"Vértice {v} - Grau entrada: {grafo2.obter_grau_entrada(v)}, "
              f"Grau saída: {grafo2.obter_grau_saida(v)}")
    print()
    
    # Teste 3: Removendo aresta
    print("3. Testando remoção de aresta:")
    print("Antes da remoção:")
    print(f"Existe aresta (1,2): {grafo1.existe_aresta(1, 2)}")
    
    grafo1.remover_aresta(1, 2)
    
    print("Depois da remoção:")
    print(f"Existe aresta (1,2): {grafo1.existe_aresta(1, 2)}")
    print(f"Vizinhos do vértice 1: {grafo1.obter_vizinhos(1)}")
    print(f"Número total de arestas: {grafo1.obter_num_arestas()}")


if __name__ == "__main__":
    main()