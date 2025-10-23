import random

def generate_large_graph(num_vertices, num_edges, file_path):
    edges = set()

    while len(edges) < num_edges:
        v1 = random.randint(0, num_vertices - 1)
        v2 = random.randint(0, num_vertices - 1)

        if v1 != v2:  # Prevenir loops
            edges.add((v1, v2, 1))  # Adiciona peso 1 por padrão

    # Salvar as arestas em um arquivo de texto
    with open(file_path, 'w') as f:
        # Escreve a primeira linha com o formato desejado
        f.write(f"{num_vertices} {num_edges} 0 0\n")
        for v1, v2, weight in edges:
            f.write(f"{v1} {v2} {weight}\n")

# Parâmetros
num_vertices = 200  # Número de vértices
num_edges = 1000     # Número de arestas
file_path = 'grafo.txt'  # Nome do arquivo de saída

# Gerar o grafo
generate_large_graph(num_vertices, num_edges, file_path)
print(f"Grafo gigante gerado e salvo em '{file_path}'.")
