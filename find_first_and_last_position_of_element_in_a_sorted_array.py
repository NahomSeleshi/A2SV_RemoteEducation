class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1,-1]
        if len(nums) == 0:
            return answer
        def binarySearchLeft(element):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    answer[0] = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
    
        def binarySearchRight(element):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] == target:
                    answer[1] = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        binarySearchLeft(target)
        binarySearchRight(target)
        return answer
