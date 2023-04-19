class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        min_boats = 0
        left, right = 0, len(people)-1
        
        while left < right:
            cur_weight = people[left] + people[right]
            if cur_weight > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            min_boats += 1

        return min_boats + 1 if left == right else min_boats