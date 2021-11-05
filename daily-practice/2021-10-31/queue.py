
class Queue:
    def __init__(self):
        self._list = []

    def size(self):
        return len(self._list)

    def queue(self, item):
        self._list.insert(0, item)

    def dequeue(self):
        if self.size() > 0:
            return self._list.pop()
        else:
            return None

    def peek(self):
        return self._list[len(self._list) - 1]

# test size initializes to 0
_queue = Queue()
assert _queue.size() == 0

# test size is 1 after adding
_queue.queue("ABC")
assert _queue.size() == 1

_queue.queue("DEF")
assert _queue.size() == 2

_queue.queue("GHI")
assert _queue.size() == 3


# test getting item from queue
_item = _queue.dequeue()
assert _item == "ABC"
assert _queue.size() == 2

# test getting item from queue
_item = _queue.dequeue()
assert _item == "DEF"
assert _queue.size() == 1

# test getting item from queue
_item = _queue.dequeue()
assert _item == "GHI"
assert _queue.size() == 0

# test getting item from queue
_item = _queue.dequeue()
assert _item == None
assert _queue.size() == 0
