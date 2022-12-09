# This is my doubly linked list node class
class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None
class MyCircularDeque:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        new_node = Node(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max_size:
            return False
        new_node = Node(value)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        return self.head.val if self.size != 0 else -1

    def getRear(self) -> int:
        return self.tail.val if self.size != 0 else -1        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()