graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    curr = queue.pop(0) 
    print(curr, end=" ") 

    for neighbour in graph[curr]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("BFS Traversal:")
bfs(visited, graph, 'A')
