class MinStack:

    def __init__(self):
        self.my_min_stack = []
        self.cur_min = float("inf")
        self.num_freq = defaultdict(int)
        
    def push(self, val: int) -> None:
        if val < self.cur_min:
            self.my_min_stack.append(self.cur_min)
            self.cur_min = val
        self.my_min_stack.append(val)
        self.num_freq[val] += 1

    def pop(self) -> None:
        cur_popped = self.my_min_stack.pop()
        self.num_freq[cur_popped] -= 1
        if ( cur_popped == self.cur_min and self.num_freq[cur_popped] == 0):
            self.cur_min = self.my_min_stack.pop()

    def top(self) -> int:
        return self.my_min_stack[-1]

    def getMin(self) -> int:
        return self.cur_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()