class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [[each[0],each[1]] for each in enumerate(nums)]
        nums_with_index.sort(key = lambda x: x[1])
        left, right = 0, len(nums)-1
        while left < right:
            curSum = nums_with_index[left][1] + nums_with_index[right][1]
            if curSum == target:
                return [nums_with_index[left][0],nums_with_index[right][0]]
            elif curSum < target:
                left += 1
            else:
                right -= 1