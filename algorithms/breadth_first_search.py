def search(G, source, destination):
    """
    This function explores all possible paths between `source` and `destination`. The
    queue, which is actually a stack, maintains all of the possible paths. The
    queue is initialized to vertex `source` and vertices adjacent to `source`
    are explored. Each path leading to the adjacent vertex is appdestinationed on to the
    queue.

    Each iteration of the while loop pops off the most recently added path. If
    that path is a dead-destination, then the loop continues which effectively discards
    the dead-destination path.

    see: http://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search#8922151
    """
    queue = []
    # Initialize the queue to the source vertex
    queue.append([source])

    # Iteration will continue until `queue` becomes an empty list
    while queue:
        path = queue.pop()
        # Get the last vertex on the path
        vertex = path[-1]

        # We found a path. It may not be the shortest path, but it's probably
        # close.
        if vertex == destination:
            return path

        # Uncomment to print the path so far. This will help visualize how BFS
        # works
        #print(path)

        # The loop below iterates over each vertex adjacent to `vertex`.
        # `get` says: "if `vertex` doesn't exist in `G`, then return an empty
        # list"
        for adjacent in G.get(vertex, []):
            # Copy the list `path` and appdestination it to the queue
            new_path = list(path)
            # Add the adjacent vertex
            new_path.append(adjacent)

            queue.append(new_path)

    # Path not found
    return None
