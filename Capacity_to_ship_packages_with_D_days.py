class Solution:

    def days_spent(self, capacity, weights):
        cur_weight = 0
        cur_days = 1

        for i in range(len(weights)):
            cur_weight += weights[i]
            if cur_weight > capacity:
                cur_weight = weights[i]
                cur_days += 1

        return cur_days



    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        least_weight = sum(weights)

        while left <= right:
            mid = left + (right - left)//2
            cur_days = self.days_spent(mid, weights)

            if cur_days > days:
                left = mid + 1

            else:
                right = mid - 1
                least_weight = min(least_weight, mid)

        return least_weight
