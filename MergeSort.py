#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        mergeArray = []
        leftIndex = l
        rightIndex = m + 1
        
        while leftIndex < m+1 and rightIndex < r + 1:
            if arr[leftIndex] < arr[rightIndex]:
                mergeArray.append(arr[leftIndex])
                leftIndex +=1
            else:
                mergeArray.append(arr[rightIndex])
                rightIndex +=1
        if leftIndex < m+1:
            while leftIndex < m + 1:
                mergeArray.append(arr[leftIndex])
                leftIndex += 1
        else:
            while rightIndex < r + 1:
                mergeArray.append(arr[rightIndex])
                rightIndex += 1
        arr[l:r+1] = mergeArray
        
    def mergeSort(self,arr, l, r):
        #code here
        if l == r:
            return
        mid = l + (r-l)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        self.merge(arr, l, mid, r)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends