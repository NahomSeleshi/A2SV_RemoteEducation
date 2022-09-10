class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return str(sorted(nums, key = lambda x: int(x))[len(nums)-k])