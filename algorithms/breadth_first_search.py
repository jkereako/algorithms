def breadth_first_search(G, S):
    visited, queue = [], [start]

    while queue:
        vertex = queue.pop()

        if vertex not in visited:
            visited.append(vertex)
            queue.extend(G[vertex] - visited)

    return visited
