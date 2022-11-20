class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_with_speed = dict(zip(position, speed))
        position.sort()
        mon_stack = []
        for i in range(len(position)-1, -1, -1):
            cur_distance = target - position[i]
            cur_time = cur_distance/pos_with_speed[position[i]]
            if not mon_stack:
                mon_stack.append(cur_time)
                continue
            if cur_time > mon_stack[-1]:
                mon_stack.append(cur_time)
        
        return len(mon_stack)