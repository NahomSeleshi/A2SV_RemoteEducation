class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_set, nums2_set = set(nums1), set(nums2)
        merged = sorted(nums1+nums2)
        for each in merged:
            if each in nums1_set and each in nums2_set:
                return each
        min_nums1 = min(nums1)
        min_nums2 = min(nums2)
 
        return int(str(min(min_nums1,min_nums2)) + str(max(min_nums1,min_nums2)))