class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_with_index = {0:-1}
        cur_mod = 0
        for index, value in enumerate(nums):
            cur_mod = (cur_mod + value) % k
            if cur_mod in mod_with_index:
                if index - mod_with_index[cur_mod] > 1:
                    return True
            else:
                mod_with_index[cur_mod] = cur_mod
        return False