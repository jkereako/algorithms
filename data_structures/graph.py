class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.relationships = {}

    def add_neighbor(self, neighbor, weight=0):
        self.relationships[neighbor] = weight

    def __str__(self):
        return str(self.key) + "connected to: " + str([x.key for x in
            self.relationships])
class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex
        self.vertex_count += 1

        return vertex

    def add_edge(self, from_v, to_v, cost=0):
        vertex = None
        if from_v not in self.vertices:
            vertex = self.add_vertex(from_v)
        if to_v not in self.vertices:
            vertex =  self.add_vertex(to_v)

        self.vertices[from_v].add_neighbor(self.vertices[to_v], cost)

    def vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]

        return None

    def __contains__(self, key):
        return key in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())

