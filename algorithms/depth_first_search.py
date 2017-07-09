def connected_components(G, source):
  visited = []
  stack = [source]

  while stack:
    # Visit newest vertex first
    vertex = stack.pop()

    if vertex not in visited:
      visited.append(vertex)
      stack.extend(G[vertex])

  return visited

def paths(G, source, destination):
  stack = [source] # Visit newest vertex first
  source_paths = [[source]] # Keeps track of all paths originating from the source
  valid_paths = [] # Valid paths from the source to the destination

  while stack:
    # We could combine these 2 values as a tuple in the stack, but it's clearer to keep them
    # separate.
    vertex = stack.pop()
    visited = source_paths.pop()
    
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
        stack.append(adjacent_vertex)
  
  return valid_paths