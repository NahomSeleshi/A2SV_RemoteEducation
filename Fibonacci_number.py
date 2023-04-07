class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return 0 if n == 0 else 1
        prev = 1
        prev_prev = 0
        for i in range(n-1):
            prev_prev, prev = prev, prev_prev + prev
        return prev
