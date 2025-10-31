class Grafo:
    def __init__(self, direcionado: bool, ponderado: bool):
        self.direcionado = direcionado
        self.ponderado = ponderado

    def ler_arquivo(self, nome_arquivo: str) -> None:
        with open(nome_arquivo, 'r') as arquivo:
            primeira_linha = arquivo.readline().strip().split()
            num_vertices = int(primeira_linha[0])
            num_arestas = int(primeira_linha[1])
            self.direcionado = bool(int(primeira_linha[2]))
            self.ponderado = bool(int(primeira_linha[3]))

            for i in range(num_vertices):
                self.inserir_vertice(str(i))  
            
            for _ in range(num_arestas):
                linha = arquivo.readline().strip()
                if not linha:  # Pula linhas vazias
                    continue
                aresta_info = linha.split()
                if len(aresta_info) < 2:  # Verifica se tem pelo menos 2 valores
                    continue
                origem = int(aresta_info[0])
                destino = int(aresta_info[1])
                peso = int(aresta_info[2]) if self.ponderado and len(aresta_info) > 2 else 1  

                self.inserir_aresta(origem, destino, peso)

    def inserir_vertice(self, label: str) -> bool:
        return

    def remover_vertice(self, label: str) -> bool:
        return

    def label_vertice(self, indice: int) -> str:
        return

    def imprime_grafo(self) -> None:
        return

    def inserir_aresta(self, origem: int, destino: int, peso: int = 1) -> bool:
        return

    def remover_aresta(self, origem: int, destino: int) -> bool:
        return

    def existe_aresta(self, origem: int, destino: int) -> bool:
        return

    def peso_aresta(self, origem: int, destino: int) -> float:
        return

    def retornar_vizinhos(self, vertice: int) -> list:
        return
