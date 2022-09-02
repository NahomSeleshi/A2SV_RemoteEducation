class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        maxIndex = len(arr)
        answer = []
        def reverseArray(index):
            left, right = 0, index-1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        while maxIndex > 1:
            curIndex = 0
            for i in range(maxIndex):
                if arr[i] > arr[curIndex]:
                    curIndex = i
            if curIndex != 0:
                answer.append(curIndex + 1)
                reverseArray(curIndex + 1)
            answer.append(maxIndex)
            reverseArray(maxIndex)
            maxIndex -= 1
        
        return answer