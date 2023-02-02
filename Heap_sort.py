#User function Template for python3

class Solution:
    
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        
        #while I have left child, which guarantees I don't have right child if not left child:)
        while (2*i) + 1 < n:
            left_child = (2*i) + 1
            right_child = (2*i) + 2 if (2*i) + 2 < n else None
            
            if right_child:
                if arr[left_child] == max(arr[left_child], arr[right_child]):
                    maximum_of_childs = left_child
                else:
                    maximum_of_childs = right_child
            else:
                maximum_of_childs = left_child
            
            if arr[i] < arr[maximum_of_childs] :
                arr[maximum_of_childs], arr[i] = arr[i], arr[maximum_of_childs]
                i = maximum_of_childs
            else:
                break
        
    #Function to build a Heap from array. It builds a max heap.
    def buildHeap(self,arr,n):
        for i in range(n-1, 0, -1):
            parent = (i-1)//2
            if arr[parent] < arr[i]:
                arr[parent], arr[i] = arr[i], arr[parent]
                self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        
        self.buildHeap(arr, n)
        for i in range(n-1, 0, -1):
            # I am building a max heap. So, the maximum will be at index 0. At every iteration, I will swap
            # the max number with the end of the list and then shrink the size of the array. After that, I 
            # will heapify the new (shrinked) array and treat it as my new array. 
            
            arr[0], arr[i] = arr[i], arr[0]
            self.heapify(arr, i, 0)
    

