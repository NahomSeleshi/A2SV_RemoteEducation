class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min, max_profit = prices[0], 0
        for each in prices:
            if each < cur_min:
                cur_min = each
            else:
                max_profit = max(max_profit, each-cur_min)
        return max_profit
    
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit, cur_min_price = 0, prices[0]
#         for each_price in prices:
#             if each_price - cur_min_price > max_profit:
#                 max_profit = each_price - cur_min_price
#             if each_price < cur_min_price:
#                 cur_min_price = each_price
#         return max_profit