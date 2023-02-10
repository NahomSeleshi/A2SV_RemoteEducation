class Solution:
    def count(self, m, n, cur_num):

        _count = 0
        for row in range(1, m+1):
            _count += min(cur_num//row, n)

        return _count

    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right, answer = 1, m*n, 1

        while left <= right:
            mid = left + (right - left)//2
            cur_count = self.count(m, n, mid)
            if cur_count < k:
                left = mid + 1
            else:
                right, answer = mid-1, mid
                
        return answer