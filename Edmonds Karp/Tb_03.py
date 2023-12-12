from collections import deque
# Edge representa uma aresta em um grafo. Ela tem um vértice de destino v, um fluxo flow, uma capacidade C e um índice reverso
# rev.
class Edge:
    def __init__(self, v, flow, C, rev): # construtor da classe Edge. inicializa um objeto Edge com um vértice de destino v, um 
                                         # fluxo flow, uma capacidade C e um índice reverso rev.
        self.v = v
        self.flow = flow
        self.C = C
        self.rev = rev

# Graph representa um grafo. Ela tem um número de vértices V e uma lista de adjacências adj que contém todas as arestas.
class Graph:
    def __init__(self, V):
        self.adj = [[] for _ in range(V)]
        self.V = V
# O método add_edge da classe Graph adiciona uma aresta ao grafo. Ele cria duas arestas (uma em cada direção) e as adiciona à 
# lista de adjacências.
    def add_edge(self, u, v, C):
        a = Edge(v, 0, C, len(self.adj[v]))
        b = Edge(u, 0, 0, len(self.adj[u]))
        self.adj[u].append(a)
        self.adj[v].append(b)
# BFS da classe Graph realiza uma busca em largura no grafo a partir de um vértice fonte até um vértice sorvedouro. Ele 
# retorna True se encontrar um caminho e False caso contrário.
    def BFS(self, s, t, parent):
        visited = [False]*self.V
        queue = deque([s])  # Use deque para melhor desempenho na remoção eficiente do início
        visited[s] = True

        while queue:
            u = queue.popleft()  # Modificado para popleft para eficiência
            for ind, i in enumerate(self.adj[u]): 
                if visited[i.v] == False and i.flow < i.C: 
                    queue.append(i.v)
                    visited[i.v] = True
                    parent[i.v] = u, ind
                    if i.v == t:
                        return True
        return False
# O método export_graph da classe Graph exporta o grafo para um arquivo. Cada linha do arquivo representa uma aresta e seu 
# fluxo correspondente.
    def export_graph(self, file_name):
        with open(file_name, 'w') as file:
            for u in range(self.V):
                for edge in self.adj[u]:
                    file.write(f'{u} {edge.v} {edge.flow}\n')
# O método FordFulkerson da classe Graph implementa o algoritmo de Ford-Fulkerson. Ele calcula o fluxo máximo entre um vértice 
# fonte e um vértice sorvedouro.
    def FordFulkerson(self, source, sink):
        parent = [-1]*self.V
        max_flow = 0
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while(s != source):
                u, ind = parent[s]
                path_flow = min(path_flow, self.adj[u][ind].C - self.adj[u][ind].flow)
                s = parent[s][0]
            max_flow += path_flow
            v = sink
            while(v != source):
                u, ind = parent[v]
                self.adj[u][ind].flow += path_flow
                self.adj[v][self.adj[u][ind].rev].flow -= path_flow
                v = parent[v][0]
        return max_flow
# A função read_graph_from_file lê um grafo de um arquivo. Ela lê o número de vértices e arestas e, em seguida, lê cada aresta e
# a adiciona ao grafo.
def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        V = int(file.readline())
        A = int(file.readline())
        g = Graph(V)
        for _ in range(A):
            u, v, C = map(float, file.readline().split())
            g.add_edge(int(u), int(v), C)
    return g


# Finalmente, o código lê um grafo de um arquivo, lê um vértice fonte e um vértice sorvedouro do usuário, calcula o fluxo
# máximo entre o vértice fonte e o vértice sorvedouro e exporta o grafo para um arquivo.
g = read_graph_from_file('C:/GRAFOS/TB_03/Tb_03.txt')

source = int(input("Digite o vértice fonte: "))
sink = int(input("Digite o vértice sorvedouro: "))

max_flow = g.FordFulkerson(source, sink)
print(f'O valor do fluxo máximo é {max_flow}')

g.export_graph('C:/GRAFOS/TB_03/Fluxo_Maximo.txt')