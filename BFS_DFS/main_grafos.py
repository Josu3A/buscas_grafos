from grafos import Graph


def carregar_grafos(fileName):
  file = open(fileName, 'r')
  num_vert = int(file.readline())

  graph = Graph(num_vert)

  linha = 0
  for line in file:
    line.strip()
    num = line.split("\t")
    coluna = 0
    for i in num:
      if (coluna == graph.num_vertices):
        break

      graph.matrix[linha][coluna] = int(i)
      if (graph.matrix[linha][coluna] > 0):
        graph.list[linha].append(coluna)

      coluna += 1

    linha += 1

  return graph

#BFS
gr = carregar_grafos('pcv4.txt')
gr.print()
dist, ant = gr.bfs(1)
print(f"\n{dist}\n")
print(f"\n{ant}\n")
gr.print_caminho(1, 6, ant)


#DFS
vertice_inic = 2
print(f"Fazendo o DFS com vértice inicial{vertice_inic}:")
gr.dfs(vertice_inic)
