


class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
b.prev_node = a
c.next_node = d
c.prev_node = b
d.next_node = e
d.prev_node = c
e.prev_node = d

def traverse(_node):
    while _node:
        print(_node.value)
        _node = _node.next_node

def traverse_reverse(_node):
    while _node:
        print(_node.value)
        _node = _node.prev_node

traverse(a)
traverse_reverse(e)
