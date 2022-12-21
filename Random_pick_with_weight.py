class Solution:

    def __init__(self, w: List[int]):
        self.my_list = list(accumulate(w))
        
    def pickIndex(self) -> int:
        
        target = random.random() * self.my_list[-1]
        left, right = 0, len(self.my_list)-1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.my_list[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()