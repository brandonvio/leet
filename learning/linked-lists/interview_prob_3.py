"""
Nth to Last Node
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def nth_to_last_node(n, head):
    left_p = head
    right_p = head

    for i in range(n - 1):
        if not right_p.nextnode:
            raise Error("N is larger than linked list")

        right_p = right_p.nextnode

    while right_p.nextnode:
        left_p = left_p.nextnode
        right_p = right_p.nextnode

    return left_p


"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    def test(self,sol):
        assert_equal(sol(2,a),d)
        print('ALL TEST CASES PASSED')

# Run tests
t = TestNLast()
t.test(nth_to_last_node)
