class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        right = 1
        curVal = nums[0]
        while right < len(nums):
            if nums[right] == curVal:
                right += 1
            else:
                nums[left] = nums[right]
                curVal = nums[right]
                left += 1
                right += 1
        return left