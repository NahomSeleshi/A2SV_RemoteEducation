
# I came up to this after a long time :)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        nums[-2] = max(nums[-2], nums[-1])
        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i]+ nums[i+2], nums[i+1])
        return nums[0]
# This is my first implementation  
# class Solution:
    
#     def give_max_money(self, cur_idx:int, memo:List[int], nums:List[int]):
#         if cur_idx >= len(nums):
#             return 0
#         if memo[cur_idx] != -1:
#             return memo[cur_idx]

#         rob = nums[cur_idx] + self.give_max_money(cur_idx + 2, memo, nums)
#         not_rob = self.give_max_money(cur_idx + 1, memo, nums)
#         max_money = max(rob, not_rob)
#         memo[cur_idx] = max_money
#         return max_money 

#     def rob(self, nums: List[int]) -> int:
#         memo = [-1 for i in range(len(nums))]
#         return self.give_max_money(0, memo, nums)