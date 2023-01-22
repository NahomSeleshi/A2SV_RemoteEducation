class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ban_D, ban_R = 0, 0
        queue = collections.deque([each for each in senate])
        vote_count = collections.Counter(senate)

        # if we have only one party
        if len(vote_count) == 1:
            return "Dire" if "D" in vote_count else "Radiant"

        while queue:
            cur_vote = queue.popleft()

            # if we have left with one party representative without any ban
            if len(queue) == 0:
                return "Dire" if cur_vote == "D" else "Radiant" 

            # if the bans for one party are greater than that party's representatives
            if ban_R > vote_count["R"] or ban_D > vote_count["D"]:
                return "Dire" if ban_R > ban_D else "Radiant"

            # if we have previous bans from "R" party members and our current vote is "D"
            if cur_vote == "D" and ban_D > 0:
                ban_D -= 1
                continue
            # if we have previous bans from "D" party members and our current vote is "R"
            if cur_vote == "R" and ban_R > 0:
                ban_R -= 1
                continue
            
            if cur_vote == "R":
                ban_D += 1
                queue.append("R")
            else:
                ban_R += 1
                queue.append("D")
