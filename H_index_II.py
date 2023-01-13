class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, len(citations)-1

        while left <= right:
            mid = left + (right - left) // 2
            right_side_elements = len(citations) - mid

            if right_side_elements == citations[mid]:
                return right_side_elements
            elif citations[mid] < right_side_elements:
                left = mid + 1
            else:
                right = mid - 1

        return len(citations) - left