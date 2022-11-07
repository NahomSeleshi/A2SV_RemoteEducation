class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.my_stack = [0]*maxSize
        self.top = -1

    def push(self, x: int) -> None:
        if not self.isFull():
            self.top += 1
            self.my_stack[self.top] = x

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        popped_element = self.my_stack[self.top]
        self.top -= 1
        return popped_element
    
    def increment(self, k: int, val: int) -> None:      
        increment_index = 0
        while increment_index <= self.top and increment_index < k:
            self.my_stack[increment_index] += val
            increment_index += 1
    
    def isFull(self):
        return self.top == self.max_size-1
    
    def isEmpty(self):
        return self.top == -1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)