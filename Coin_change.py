class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        visited_coins = set(coins)
        queue = deque(coins)
        fewest_coins = 1
        
        while queue:
            for i in range(len(queue)):
                cur_coin = queue.popleft()
                if cur_coin == amount:
                    return fewest_coins
                for each in coins:
                    possible_coin = each + cur_coin
                    if possible_coin not in visited_coins and possible_coin <= amount:
                        queue.append(possible_coin)
                        visited_coins.add(possible_coin)
            fewest_coins += 1

        return -1
