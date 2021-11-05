
class Stack:
    def __init__(self):
        self._list = []

    def size(self):
        return len(self._list)

    def push(self, item):
        self._list.append(item)

    def pop(self):
        return self._list.pop()

_stack = Stack()
assert _stack.size() == 0
_stack.push("ABC")
assert _stack.size() == 1
_item = _stack.pop()
assert _item == "ABC"
