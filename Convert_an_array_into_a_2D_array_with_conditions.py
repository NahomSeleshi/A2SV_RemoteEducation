class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_freq = collections.Counter(nums)
        buckets_number = max(num_freq.values())
        
        list_dict = defaultdict(list)
        num_bucket_index = {}
        for each in set(nums):
            num_bucket_index[each] = 0
        for each in nums:
            list_dict[num_bucket_index[each]].append(each)
            num_bucket_index[each] += 1
    
        return [each_bucket for each_bucket in list_dict.values()]