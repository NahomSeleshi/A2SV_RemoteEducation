class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right):
            if left > right:
                return left
            mid = left + (right - left)//2
            if nums[mid] < target:
                index = binarySearch(mid+1, right)
            else:
                index = binarySearch(left, mid-1)
            return index
        return binarySearch(0,len(nums)-1)