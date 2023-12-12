import sys
# Construtor da classe Grafo. Ele inicializa o grafo com o número especificado de vértices e cria uma lista 
# vazia para armazenar as arestas do grafo.E ele inicializa uma lista de predecessores com -1, que 
# será usada para rastrear o caminho mais curto.
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []
        self.predecessores = [-1] * vertices
        
# Função para adicionar uma aresta ao grafo. Recebe aresta, vértice e peso e adicona à aresta que é uma lista 
# com esses 3 elementos.
    def adiciona_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

 # Função imprime o caminho mais curto da origem até o vértice v. Ela faz isso recursivamente, rastreando o
 # predecessor de cada vértice até chegar à origem.
    def imprime_caminho(self, v, caminho):
        if self.predecessores[v] != -1:
            self.imprime_caminho(self.predecessores[v], caminho)
        caminho.append(v)

# Implementação do algoritmo de Bellman-Ford. Ele calcula as distâncias mais curtas da origem para todos os 
# outros vértices no grafo. Se detectar um ciclo de peso negativo, ele imprime uma mensagem de erro.
    def bellman_ford(self, origem):
        dist = [float("Inf")] * self.V
        dist[origem] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.grafo:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    self.predecessores[v] = u

        for u, v, w in self.grafo:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("O grafo contém um ciclo de peso negativo")
                return

        return dist

# Função gera um arquivo que representa o subgrafo do grafo original. O subgrafo contém apenas as arestas que
# fazem parte do caminho mais curto da origem para todos os outros vértices.
    def gera_arquivo_subgrafo(self, nome_arquivo):
        with open(nome_arquivo, 'w') as arquivo:
            for v in range(self.V):
                if self.predecessores[v] != -1:
                    arquivo.write(f"{self.predecessores[v]} {v}\n")

# Função auxiliar fora da classe Grafo. Ela lê um grafo de um arquivo. O arquivo deve conter o número de 
# vértices na primeira linha e as arestas nas linhas subsequentes. Cada aresta é representada por três números:
# o vértice de origem, o vértice de destino e o peso da aresta.
def le_grafo_do_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        V = int(linhas[0].strip())
        g = Grafo(V)    
        for linha in linhas[2:]:
            u, v, w = map(float, linha.strip().split())
            g.adiciona_aresta(int(u), int(v), w)
        return g

if __name__ == "__main__":
    caminho_arquivo = "C:/GRAFOS/TB_02_txt" 
    g = le_grafo_do_arquivo(caminho_arquivo)
    distancias = g.bellman_ford(0)
    print("Distâncias mínimas da origem para todos os vértices:")
    for i in range(g.V):
        print(f"{i}: {round(distancias[i], 2)}")

    print("\nCaminho mínimo da origem para o vértice 4:")
    caminho = []
    g.imprime_caminho(4, caminho)
    print(' '.join(map(str, caminho)))
    g.gera_arquivo_subgrafo("subgrafo.txt")

