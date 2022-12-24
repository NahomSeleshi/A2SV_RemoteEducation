class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        current_fruits, max_fruits, distinct_fruits = 0, 0, 0
        left, right = 0, 0
        while right < len(fruits):
            if not fruit_count[fruits[right]] and distinct_fruits < 2:
                distinct_fruits += 1
                fruit_count[fruits[right]] = 1
                current_fruits += 1
                right +=1
            elif fruit_count[fruits[right]]:
                fruit_count[fruits[right]] += 1
                current_fruits += 1
                right += 1
            else:
                max_fruits = max(max_fruits, current_fruits)
                fruit_count[fruits[left]] -= 1
                if not fruit_count[fruits[left]]:
                    distinct_fruits -= 1
                current_fruits -= 1
                left += 1
        max_fruits = max(max_fruits, current_fruits)
        return max_fruits






