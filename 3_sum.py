class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        numsSet = set(nums)
        visited, innerVisited = set(), set()
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum == -nums[i]:
                    if not nums[left] in innerVisited and not nums[right] in innerVisited:
                        answer.append([nums[i], nums[left], nums[right]])
                        innerVisited.add(nums[left])
                        innerVisited.add(nums[right])
                    left += 1
                    right -= 1
                elif curSum > -nums[i]:
                    right -= 1
                else:
                    left += 1
            innerVisited.clear()
            visited.add(nums[i])
                    
        return answer