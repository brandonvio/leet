import typing


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}

    def add_neighbor(self, nbr, weight=0):
        self.connections[nbr] = weight

    def get_connections(self):
        return self.connections.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connections[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x for x in self.connections])


class Graph:
    def __init__(self):
        self.vertices: typing.Dict[int, Vertex] = {}
        self.vertices_count = 0

    def add_vertex(self, key):
        self.vertices_count += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def add_edge(self, f, t, cost=0):
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(t, cost)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, item):
        return item in self.vertices

    def __str__(self):
        _str = ""
        for v in self.vertices:
            _str += str(self.vertices[v]) + "\n"
        return _str
