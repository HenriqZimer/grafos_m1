"""
Trabalho M1 - Parte 1: Implementação de Grafos
Implementação conforme especificação dos slides S02 - Conceitos Básicos e Representação
Autor: Henrique Zimermann
Data: 12 de setembro de 2025
"""

class Aresta:
    """
    Estrutura auxiliar para representar uma aresta
    """
    def __init__(self, destino, peso=1):
        self.destino = destino
        self.peso = peso
    
    def __str__(self):
        return f"({self.destino}, {self.peso})"
    
    def __repr__(self):
        return self.__str__()


class Grafo:
    """
    Classe base para grafos
    O construtor deve pedir duas informações:
    - Se é Direcionado ou não
    - Se é Ponderado ou não
    """
    
    def __init__(self, direcionado=False, ponderado=False):
        """
        Inicializa o grafo
        
        Args:
            direcionado (bool): Se o grafo é direcionado ou não
            ponderado (bool): Se o grafo é ponderado ou não
        """
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.vertices = []  # Lista de labels dos vértices
    
    def inserirVertice(self, label):
        """
        Adiciona um vértice sem nenhuma aresta associada a ele
        
        Args:
            label (str): Nome/label do vértice
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def removerVertice(self, indice):
        """
        Remove um vértice do grafo, elimina todas as arestas que chegam e saem dele
        
        Args:
            indice (int): Índice do vértice a ser removido
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def labelVertice(self, indice):
        """
        Retorna o nome de um vértice
        
        Args:
            indice (int): Índice do vértice
            
        Returns:
            str: Label do vértice
        """
        if 0 <= indice < len(self.vertices):
            return self.vertices[indice]
        return None
    
    def imprimeGrafo(self):
        """
        Imprime o grafo no console
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def inserirAresta(self, origem, destino, peso=1):
        """
        Insere uma aresta entre dois vértices
        Deve considerar se o grafo é direcionado e ponderado
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            peso (float): Peso da aresta (default=1)
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def removerAresta(self, origem, destino):
        """
        Remove uma aresta entre dois vértices
        No grafo não direcionado deve ser removida a aresta de retorno também
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def existeAresta(self, origem, destino):
        """
        Verifica a existência de uma aresta
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se existe a aresta, False caso contrário
        """
        raise NotImplementedError("Método deve ser implementado nas subclasses")
    
    def _indiceValido(self, indice):
        """
        Verifica se um índice de vértice é válido
        
        Args:
            indice (int): Índice do vértice
            
        Returns:
            bool: True se válido, False caso contrário
        """
        return 0 <= indice < len(self.vertices)

class GrafoMatriz(Grafo):
    """
    Especialização que usa uma matriz de adjacência como representação do grafo
    """
    
    def __init__(self, direcionado=False, ponderado=False):
        """
        Inicializa o grafo com representação por matriz
        
        Args:
            direcionado (bool): Se o grafo é direcionado ou não
            ponderado (bool): Se o grafo é ponderado ou não
        """
        super().__init__(direcionado, ponderado)
        self.matriz = []  # Matriz de adjacência (será expandida dinamicamente)
    
    def inserirVertice(self, label):
        """
        Adiciona um vértice sem nenhuma aresta associada a ele
        Adiciona o vértice no vetor de vértices e aloca espaço na matriz
        
        Args:
            label (str): Nome/label do vértice
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        if label in self.vertices:
            return False  # Vértice já existe
        
        # Adiciona o vértice
        self.vertices.append(label)
        n = len(self.vertices)
        
        # Expande a matriz para o novo tamanho
        # Primeiro adiciona uma nova coluna para cada linha existente
        for i in range(n - 1):
            self.matriz[i].append(0)
        
        # Adiciona uma nova linha para o novo vértice
        self.matriz.append([0] * n)
        
        return True
    
    def removerVertice(self, indice):
        """
        Remove um vértice do grafo, elimina a linha e coluna dele da matriz
        e todas as arestas que chegam e saem dele
        
        Args:
            indice (int): Índice do vértice a ser removido
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        if not self._indiceValido(indice):
            return False
        
        # Remove o vértice da lista
        self.vertices.pop(indice)
        
        # Remove a linha correspondente
        self.matriz.pop(indice)
        
        # Remove a coluna correspondente
        for i in range(len(self.matriz)):
            self.matriz[i].pop(indice)
        
        return True
    
    def imprimeGrafo(self):
        """
        Imprime o grafo no console usando representação por matriz
        """
        print("Grafo (Matriz de Adjacência):")
        print(f"Tipo: {'Direcionado' if self.direcionado else 'Não direcionado'}, "
              f"{'Ponderado' if self.ponderado else 'Não ponderado'}")
        print(f"Vértices: {self.vertices}")
        
        if not self.vertices:
            print("Grafo vazio")
            return
        
        # Cabeçalho da matriz
        print("\n     ", end="")
        for i, label in enumerate(self.vertices):
            print(f"{label:>4}", end="")
        print()
        
        # Linhas da matriz
        for i, label in enumerate(self.vertices):
            print(f"{label:>4}:", end="")
            for j in range(len(self.vertices)):
                print(f"{self.matriz[i][j]:>4}", end="")
            print()
    
    def inserirAresta(self, origem, destino, peso=1):
        """
        Insere uma aresta entre dois vértices na matriz
        Considera se o grafo é direcionado e ponderado
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            peso (float): Peso da aresta (default=1)
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        # Define o peso da aresta
        peso_aresta = peso if self.ponderado else 1
        
        # Insere a aresta
        self.matriz[origem][destino] = peso_aresta
        
        # Se não é direcionado, adiciona a aresta de volta
        if not self.direcionado:
            self.matriz[destino][origem] = peso_aresta
        
        return True
    
    def removerAresta(self, origem, destino):
        """
        Remove uma aresta entre dois vértices da matriz
        No grafo não direcionado remove a aresta de retorno também
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        # Remove a aresta
        self.matriz[origem][destino] = 0
        
        # Se não é direcionado, remove a aresta de volta
        if not self.direcionado:
            self.matriz[destino][origem] = 0
        
        return True
    
    def existeAresta(self, origem, destino):
        """
        Verifica a existência de uma aresta na matriz
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se existe a aresta, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        return self.matriz[origem][destino] != 0

class GrafoLista(Grafo):
    """
    Especialização que usa uma lista de adjacência como representação do grafo
    e tem uma estrutura Aresta como auxílio
    """
    
    def __init__(self, direcionado=False, ponderado=False):
        """
        Inicializa o grafo com representação por lista de adjacência
        
        Args:
            direcionado (bool): Se o grafo é direcionado ou não
            ponderado (bool): Se o grafo é ponderado ou não
        """
        super().__init__(direcionado, ponderado)
        self.listas = []  # Lista de listas de adjacência
    
    def inserirVertice(self, label):
        """
        Adiciona um vértice sem nenhuma aresta associada a ele
        Adiciona o vértice no vetor de vértices e aloca espaço para as arestas
        
        Args:
            label (str): Nome/label do vértice
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        if label in self.vertices:
            return False  # Vértice já existe
        
        # Adiciona o vértice
        self.vertices.append(label)
        
        # Adiciona uma nova lista de adjacência para o novo vértice
        self.listas.append([])
        
        return True
    
    def removerVertice(self, indice):
        """
        Remove um vértice do grafo, elimina a referência dele da lista
        e todas as arestas que chegam e saem dele
        
        Args:
            indice (int): Índice do vértice a ser removido
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        if not self._indiceValido(indice):
            return False
        
        # Remove todas as arestas que chegam no vértice
        for i in range(len(self.listas)):
            self.listas[i] = [aresta for aresta in self.listas[i] 
                             if aresta.destino != indice]
        
        # Atualiza os índices das arestas após a remoção
        for i in range(len(self.listas)):
            for aresta in self.listas[i]:
                if aresta.destino > indice:
                    aresta.destino -= 1
        
        # Remove o vértice e sua lista de adjacência
        self.vertices.pop(indice)
        self.listas.pop(indice)
        
        return True
    
    def imprimeGrafo(self):
        """
        Imprime o grafo no console usando representação por lista de adjacência
        """
        print("Grafo (Lista de Adjacência):")
        print(f"Tipo: {'Direcionado' if self.direcionado else 'Não direcionado'}, "
              f"{'Ponderado' if self.ponderado else 'Não ponderado'}")
        
        if not self.vertices:
            print("Grafo vazio")
            return
        
        print("Vértices e suas adjacências:")
        for i, label in enumerate(self.vertices):
            arestas_str = []
            for aresta in self.listas[i]:
                destino_label = self.vertices[aresta.destino]
                if self.ponderado:
                    arestas_str.append(f"{destino_label}({aresta.peso})")
                else:
                    arestas_str.append(destino_label)
            
            print(f"{label}: [{', '.join(arestas_str)}]")
    
    def inserirAresta(self, origem, destino, peso=1):
        """
        Insere uma aresta entre dois vértices na lista
        Considera se o grafo é direcionado e ponderado
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            peso (float): Peso da aresta (default=1)
            
        Returns:
            bool: True se inseriu com sucesso, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        # Verifica se a aresta já existe
        for aresta in self.listas[origem]:
            if aresta.destino == destino:
                return False  # Aresta já existe
        
        # Define o peso da aresta
        peso_aresta = peso if self.ponderado else 1
        
        # Insere a aresta
        self.listas[origem].append(Aresta(destino, peso_aresta))
        
        # Se não é direcionado, adiciona a aresta de volta
        if not self.direcionado:
            # Verifica se a aresta de volta já existe
            existe_volta = False
            for aresta in self.listas[destino]:
                if aresta.destino == origem:
                    existe_volta = True
                    break
            
            if not existe_volta:
                self.listas[destino].append(Aresta(origem, peso_aresta))
        
        return True
    
    def removerAresta(self, origem, destino):
        """
        Remove uma aresta entre dois vértices da lista
        No grafo não direcionado remove a aresta de retorno também
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se removeu com sucesso, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        # Remove a aresta da origem para o destino
        self.listas[origem] = [aresta for aresta in self.listas[origem] 
                              if aresta.destino != destino]
        
        # Se não é direcionado, remove a aresta de volta
        if not self.direcionado:
            self.listas[destino] = [aresta for aresta in self.listas[destino] 
                                   if aresta.destino != origem]
        
        return True
    
    def existeAresta(self, origem, destino):
        """
        Verifica a existência de uma aresta na lista
        
        Args:
            origem (int): Índice do vértice de origem
            destino (int): Índice do vértice de destino
            
        Returns:
            bool: True se existe a aresta, False caso contrário
        """
        if not self._indiceValido(origem) or not self._indiceValido(destino):
            return False
        
        for aresta in self.listas[origem]:
            if aresta.destino == destino:
                return True
        
        return False



def main():
    """
    Função principal para testar a implementação conforme especificações dos slides
    """
    print("=== Teste da Implementação de Grafos - Slides S02 ===\n")
    
    # Teste 1: GrafoMatriz não direcionado e não ponderado
    print("1. Testando GrafoMatriz - Não direcionado, Não ponderado:")
    grafo_matriz = GrafoMatriz(direcionado=False, ponderado=False)
    
    # Inserindo vértices
    print("Inserindo vértices A, B, C, D:")
    grafo_matriz.inserirVertice("A")
    grafo_matriz.inserirVertice("B")
    grafo_matriz.inserirVertice("C")
    grafo_matriz.inserirVertice("D")
    
    # Inserindo arestas
    print("Inserindo arestas (A-B), (A-C), (B-D), (C-D):")
    grafo_matriz.inserirAresta(0, 1)  # A-B
    grafo_matriz.inserirAresta(0, 2)  # A-C
    grafo_matriz.inserirAresta(1, 3)  # B-D
    grafo_matriz.inserirAresta(2, 3)  # C-D
    
    grafo_matriz.imprimeGrafo()
    
    # Testando funções básicas
    print("\nTestes das funções básicas:")
    print(f"Label do vértice 0: {grafo_matriz.labelVertice(0)}")
    print(f"Label do vértice 2: {grafo_matriz.labelVertice(2)}")
    print(f"Existe aresta A-B (0-1): {grafo_matriz.existeAresta(0, 1)}")
    print(f"Existe aresta A-D (0-3): {grafo_matriz.existeAresta(0, 3)}")
    
    print("\n" + "="*60 + "\n")
    
    # Teste 2: GrafoLista direcionado e ponderado
    print("2. Testando GrafoLista - Direcionado, Ponderado:")
    grafo_lista = GrafoLista(direcionado=True, ponderado=True)
    
    # Inserindo vértices
    print("Inserindo vértices X, Y, Z:")
    grafo_lista.inserirVertice("X")
    grafo_lista.inserirVertice("Y")
    grafo_lista.inserirVertice("Z")
    
    # Inserindo arestas com pesos
    print("Inserindo arestas com pesos (X->Y:5), (X->Z:3), (Y->Z:2):")
    grafo_lista.inserirAresta(0, 1, 5)  # X->Y peso 5
    grafo_lista.inserirAresta(0, 2, 3)  # X->Z peso 3
    grafo_lista.inserirAresta(1, 2, 2)  # Y->Z peso 2
    
    grafo_lista.imprimeGrafo()
    
    # Testando funções básicas
    print("\nTestes das funções básicas:")
    print(f"Label do vértice 1: {grafo_lista.labelVertice(1)}")
    print(f"Existe aresta X->Y (0->1): {grafo_lista.existeAresta(0, 1)}")
    print(f"Existe aresta Y->X (1->0): {grafo_lista.existeAresta(1, 0)}")
    
    print("\n" + "="*60 + "\n")
    
    # Teste 3: Remoção de arestas
    print("3. Testando remoção de arestas:")
    print("Removendo aresta A-C (0-2) do grafo matriz:")
    print(f"Antes: Existe aresta A-C: {grafo_matriz.existeAresta(0, 2)}")
    grafo_matriz.removerAresta(0, 2)
    print(f"Depois: Existe aresta A-C: {grafo_matriz.existeAresta(0, 2)}")
    
    print("\nGrafo após remoção:")
    grafo_matriz.imprimeGrafo()
    
    print("\n" + "="*60 + "\n")
    
    # Teste 4: Remoção de vértices
    print("4. Testando remoção de vértices:")
    print("Removendo vértice Y (índice 1) do grafo lista:")
    grafo_lista.removerVertice(1)
    
    print("\nGrafo após remoção do vértice:")
    grafo_lista.imprimeGrafo()
    
    print("\n" + "="*60 + "\n")
    
    # Teste 5: Comparação entre representações
    print("5. Comparação entre representações - Mesmo grafo:")
    
    # Criando o mesmo grafo com ambas as representações
    matriz_comp = GrafoMatriz(direcionado=False, ponderado=True)
    lista_comp = GrafoLista(direcionado=False, ponderado=True)
    
    vertices = ["Alpha", "Beta", "Gamma"]
    arestas = [(0, 1, 10), (0, 2, 20), (1, 2, 30)]
    
    # Inserindo nos dois grafos
    for v in vertices:
        matriz_comp.inserirVertice(v)
        lista_comp.inserirVertice(v)
    
    for origem, destino, peso in arestas:
        matriz_comp.inserirAresta(origem, destino, peso)
        lista_comp.inserirAresta(origem, destino, peso)
    
    print("Representação por Matriz:")
    matriz_comp.imprimeGrafo()
    
    print("\nRepresentação por Lista:")
    lista_comp.imprimeGrafo()
    
    # Verificando consistência
    print("\nVerificação de consistência:")
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            matriz_existe = matriz_comp.existeAresta(i, j)
            lista_existe = lista_comp.existeAresta(i, j)
            if matriz_existe != lista_existe:
                print(f"INCONSISTÊNCIA: ({i},{j}) - Matriz:{matriz_existe}, Lista:{lista_existe}")
            elif matriz_existe:
                print(f"Aresta {vertices[i]}-{vertices[j]}: Ambas representações concordam")


if __name__ == "__main__":
    main()