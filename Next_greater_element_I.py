class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = defaultdict(int)
        my_stack = []
        for each in nums2:
            if len(my_stack) == 0:
                my_stack.append(each)
            else:
                while my_stack and my_stack[-1] < each:
                    next_greater[my_stack.pop()] = each
                my_stack.append(each)
        while my_stack:
            next_greater[my_stack.pop()] = -1
        
        return [next_greater[each] for each in nums1]