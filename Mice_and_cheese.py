class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward_difference = []
        for i in range(len(reward1)):
            reward_difference.append((reward1[i]-reward2[i], i))
        reward_difference.sort(reverse = True)
        
        max_points = 0
        for i in range(len(reward_difference)):
            if i < k:
                max_points += reward1[reward_difference[i][1]]
            else:
                max_points += reward2[reward_difference[i][1]]
        
        return max_points