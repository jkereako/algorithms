def connected_components(G, source):
  visited = []
  queue = [source]

  while queue:
    # Visit oldest vertex first
    vertex = queue.pop(0)

    if vertex not in visited:
      visited.append(vertex)
      queue.extend(G[vertex])

  return visited

def paths(G, source, destination):
  queue = [source] # Visit oldest vertex first
  source_paths = [[source]] # Keeps track of all paths originating from the source
  valid_paths = [] # Valid paths from the source to the destination

  while queue:
    vertex = queue.pop(0)
    visited = source_paths.pop(0)
    
    # DEBUG:
    # print("Vertex: " + vertex)
    # print("Adjacent edges: " + str(set(G[vertex])))
    # print("Visited: " + str(set(visited)))
    # print("Not visited: " + str(set(G[vertex]) - set(visited)) + "\n")
    
    # Visit adjacent vertices
    for adjacent_vertex in G[vertex]:
      if adjacent_vertex in visited:
        continue
      
      path = visited + [adjacent_vertex]
      
      if adjacent_vertex == destination:
        valid_paths.append(path)

      else:
        source_paths.append(path)
        queue.append(adjacent_vertex)
  
  return valid_paths
