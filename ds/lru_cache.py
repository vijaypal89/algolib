MAX_LRU_LEN = 16

class DLL:
    """
    Doubly Linked List
    """
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class LRUCache:
    def __init__(self, size=MAX_LRU_LEN):
        self.head = None
        self.tail = None
        self.map = {}
        self.size = size

    def pop(self):
        """
        Remove element from end
        """
        if self.tail is None:
            return
        prev = self.tail.prev
        value = self.tail.data
        if self.tail.prev is not None:
            self.tail.prev.next = self.tail.next
        self.tail = prev
        return value

    def refer(self, key):
        # Add key into cache
        if key not in self.map:
            if len(self.map) == self.size:
                # Remove last since cache is full
                value = self.pop()
                del(self.map[value])
            new_node = DLL(key)
            new_node.next = self.head
            new_node.prev = None
            if self.head is not None:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
        else:
            # update cache, move the key on front
            node = self.map[key]
            if node != self.head:
                if node == self.tail:
                    self.tail = node.prev
                if node.next is not None:
                    node.next.prev = node.prev
                if node.prev is not None:
                    node.prev.next = node.next

                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node

        self.map[key] = self.head

    def printit(self):
        node = self.head
        while node:
            print node.data
            node = node.next

lru = LRUCache(size=3)

lru.refer(1)
lru.refer(2)
lru.refer(4)
lru.refer(5)
lru.refer(1)
lru.printit(); print "\n"
lru.refer(4)
lru.printit(); print "\n"
lru.refer(1)
lru.printit(); print "\n"

