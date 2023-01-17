class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right  = 1, len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid -1
        return left