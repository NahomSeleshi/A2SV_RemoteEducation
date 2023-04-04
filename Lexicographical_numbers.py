class Solution:
    def dfs(self, cur_num:str, nums_list:list, n:int, lexi_nums:list) -> list:
        if int(cur_num) > n:
            return lexi_nums
        lexi_nums.append(int(cur_num))

        for each_num in nums_list:
            lexi_nums = self.dfs(str(cur_num) + each_num, nums_list, n, lexi_nums)

        return lexi_nums
    def lexicalOrder(self, n: int) -> List[int]:
        
        final_lexi_nums = []
        nums_list = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        for each in nums:
            final_lexi_nums = self.dfs(each, nums_list, n, final_lexi_nums)
        
        return final_lexi_nums
