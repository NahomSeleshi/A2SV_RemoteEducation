class FrontMiddleBackQueue:

    def __init__(self):
        self.left = collections.deque([])
        self.right = collections.deque([])

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance_sizes()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        self.left.append(val)
        self.balance_sizes()

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance_sizes()

    def popFront(self) -> int:
        val = self.left.popleft() if self.left else -1
        self.balance_sizes()
        return val

    def popMiddle(self) -> int:
        val = self.left.pop() if self.left else -1
        self.balance_sizes()
        return val

    def popBack(self) -> int:
        val = (self.right or self.left or [-1]).pop()
        self.balance_sizes()
        return val
    def balance_sizes(self):
        if len(self.left) > len(self.right) + 1:
            self.right.appendleft(self.left.pop())
        if self.right and len(self.right) > len(self.left):
            self.left.append(self.right.popleft())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()