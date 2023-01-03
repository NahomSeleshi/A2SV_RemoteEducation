class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        one_third = len(nums) // 3
        num_freq = collections.Counter(nums)
        answer = []
        for each_key in num_freq:
            if num_freq[each_key] > one_third:
                answer.append(each_key)
        return answer