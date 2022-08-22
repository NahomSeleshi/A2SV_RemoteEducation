class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer, leftIndex, rightIndex, turn = [],0,n,'L'
        while rightIndex < len(nums):
            if turn == 'L':
                answer.append(nums[leftIndex])
                turn = 'R'
                leftIndex += 1
            else:
                answer.append(nums[rightIndex])
                turn = 'L'
                rightIndex += 1
        return answer