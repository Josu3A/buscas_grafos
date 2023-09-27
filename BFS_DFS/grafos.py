import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]


    def print(self):
        print(self.matrix)
        print(self.list)


    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        isVisited[source] = True
        dist[source] = 0
        fila = queue.Queue()
        fila.put(source)

        while fila.empty() != True:
            p = fila.get()
            for v in self.list[p]:
                if (isVisited[v] == False):
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    fila.put(v)
                    isVisited[v] = True

        return dist, ant 


      # 's' = vértice de origem e 't' = vértice final
    def print_caminho(self, s, t, ant):
        #verifica se não exixte caminho de 's' até 't' 
        if ant[t] == -1:
            print("Não existe caminho entre os vértices.")
            return
        #lista que armazena os vértices no caminho entre 's' e 't'
        vertices_caminho = []
        #loop para percorrer os vértices no caminho de 't' até o 's'. 
        while t != s:
            vertices_caminho.append(t)
            t = ant[t]
            #o 's' é adicionado à lista path
        vertices_caminho.append(s)
        #a lista é invertida, para ficar na ordem correta
        vertices_caminho.reverse()
        print("\nCaminho entre os vértices:")
        print(" -> ".join(map(str, vertices_caminho)))
    
    def dfs(self, source):
        visitados = set() # add vertices já visitados
        pilha = [source] #pilha tem add o vertice inicial 

        while pilha:
            vertice = pilha.pop() #tira do topo
            if vertice not in visitados:
                print(vertice, end=" ")
                visitados.add(vertice) #marca como visitado

            for vizinho in reversed(self.list[vertice]): #pega invertido na pilha todos os vizinhos ao vertice para ficar já na ordem correta
                if vizinho not in visitados:
                    pilha.append(vizinho)
