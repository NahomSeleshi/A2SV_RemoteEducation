class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenIndex, oddIndex = 0,1
        nums1 = nums.copy()
        for i in range(len(nums)):
            curNum = nums1.pop()
            if curNum % 2 == 0:
                nums[evenIndex] = curNum
                evenIndex += 2
            else:
                nums[oddIndex] = curNum
                oddIndex += 2
        return nums

# This is also a possible solution
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        numHolder = defaultdict(list)
        for each in nums:
            if each % 2 == 0:
                numHolder["Even"].append(each)
            else:
                numHolder["Odd"].append(each)
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = numHolder["Even"].pop()
            else:
                nums[i] = numHolder["Odd"].pop()
        return nums

#But, the best solution is the one below. It is O(n) in time and O(1) in space
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenIndex, oddIndex = 0,1
        listSize = len(nums)
        
        while evenIndex < listSize and oddIndex < listSize:
            if nums[evenIndex] % 2 == 0:
                evenIndex += 2
            elif nums[oddIndex] % 2 == 1:
                oddIndex += 2
            else:
                nums[evenIndex], nums[oddIndex] = nums[oddIndex], nums[evenIndex]
                evenIndex += 2
                oddIndex += 2
        return nums