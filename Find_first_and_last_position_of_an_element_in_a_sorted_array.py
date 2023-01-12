class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.answer = [-1, -1]
        if len(nums) == 0:
            return self.answer

        self.binary_search_left(nums, target)
        self.binary_search_right(nums, target)

        return self.answer

    def binary_search_left(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                self.answer[0] = mid
                right = mid - 1
            elif array[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

    def binary_search_right(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                self.answer[1] = mid
                left = mid + 1
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
