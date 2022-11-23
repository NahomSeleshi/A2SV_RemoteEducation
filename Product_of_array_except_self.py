class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix_product, right_prefix_product = [1],[1]
        for i in range(n):
            left_prefix_product.append(left_prefix_product[-1] * nums[i])
        left_prefix_product.append(1)
        
        for j in range(n-1, -1, -1):
            right_prefix_product.append(right_prefix_product[-1] * nums[j])
        right_prefix_product.append(1)
        right_prefix_product.reverse()
        
        answer = []
        for i in range(1, n+1):
            answer.append(left_prefix_product[i-1] * right_prefix_product[i+1])
        return answer