class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait_days = [0]*len(temperatures)
        index_stack = []
        
        for i in range(len(temperatures)):
            while index_stack and temperatures[i] > temperatures[index_stack[-1][0]]:
                cur_popped_index = index_stack.pop()[0]
                wait_days[cur_popped_index] = i - cur_popped_index
                
            index_stack.append((i, temperatures[i]))
                               
        return wait_days