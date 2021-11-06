import collections
from enum import Enum
from typing import Dict, OrderedDict


class State(Enum):
    unvisted = 0
    visited = 1
    visiting = 3


class Node:
    def __init__(self, id: int):
        self.id: int = id
        self.visit_state: State = State.unvisted
        self.adjacent: OrderedDict[Node, int] = collections.OrderedDict()  # key = node, value = weight

    def __str__(self):
        return "node:" + str(self.id) + \
               " visit_state:" + str(self.visit_state) + \
               " edge_count:" + str(len(self.adjacent))


class Graph2:
    def __init__(self):
        self.nodes: OrderedDict[int, Node] = collections.OrderedDict()

    def add_node(self, id):
        node = Node(id)
        self.nodes[id] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)

        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight

    def __str__(self):
        _str = ""
        print("")
        for v in self.nodes:
            _str += str(self.nodes[v]) + "\n"

        return _str
