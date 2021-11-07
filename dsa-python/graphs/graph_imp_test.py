from graph_imp_1 import Graph, Vertex
from graph_imp_2 import Graph2, Node
from collections import OrderedDict


def test_graph():
    g = Graph()
    assert g

    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1, 10)
    g.add_edge(1, 2, 9)

    v0 = g.vertices[0]
    assert v0.connections


def test_graph2():
    g = Graph2()
    g.add_edge(11, 12, 5)
    assert len(g.nodes) == 2
    assert g.nodes[11].id == 11
    assert g.nodes[12].id == 12
    assert g.nodes[11].adjacent[g.nodes[12]] == 5


def test_dfs_graph():
    def dfs(graph, start):
        visited_ordered = OrderedDict()
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited_ordered[vertex] = 1
                visited.add(vertex)
                stack.extend(graph[vertex] - visited)

        return visited_ordered

    graph = {'A': set(['C', 'B']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    result = dfs(graph, "A")
    # print(result)


def test_bfs_graph():
    def bfs(graph, start):
        visited_ordered = OrderedDict()
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited_ordered[vertex] = 1
                visited.add(vertex)
                queue.extend(graph[vertex] - visited)

        return visited_ordered

    graph = {'A': set(['C', 'B']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    result = bfs(graph, "A")
    # print(result)
