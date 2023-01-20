class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        my_stack = []
        max_area = 0
        for cur_index, cur_bar in enumerate(heights):

            # left_most_index is the index that our current bar has a height that is
            # greater than or equal to our current height
            left_most_index, left_most_bar = cur_index, cur_bar
            
            while my_stack and my_stack[-1][1] >= cur_bar:
                left_most_index, left_most_bar = my_stack.pop()
                max_area = max(max_area, (cur_index - left_most_index)*left_most_bar)

            my_stack.append([left_most_index, cur_bar])
        
        for cur_index, cur_bar in my_stack:
            max_area = max(max_area, (len(heights)-cur_index) * cur_bar)

        return max_area
