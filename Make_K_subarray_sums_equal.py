class Solution:

    def min_moves(self, cur_arr):
        median = sorted(cur_arr)[len(cur_arr)//2]
        return sum(abs(cur_num - median) for cur_num in cur_arr)

    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
        min_operations = 0
        gcd_ = math.gcd(len(arr), k)
        for i in range(gcd_):
            sub_array = []
            for j in range(len(arr)//gcd_):
                cur_idx = (gcd_*j) + i
                sub_array.append(arr[cur_idx])
            min_operations += self.min_moves(sub_array)

        return min_operations