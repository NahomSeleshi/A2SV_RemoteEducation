class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        even_turbulance, odd_turbulance = 0, 0
        current_turbulance = 1

        # This is for even turbulance which means current value is 
        # greater than next value when the current index is even
        for i in range(len(arr)-1):
            if (i%2 and arr[i] < arr[i+1]) or (not i%2 and arr[i] > arr[i+1]):
                current_turbulance += 1
            else:
                current_turbulance = 1
            even_turbulance = max(even_turbulance, current_turbulance)

        # This is for odd turbulance which means current value is 
        # greater than next value when the current index is odd
        current_turbulance = 1
        for j in range(len(arr)-1):
            if (j%2 and arr[j] > arr[j+1]) or (not j%2 and arr[j] < arr[j+1]):
                current_turbulance += 1
            else:
                current_turbulance = 1
            odd_turbulance = max(odd_turbulance, current_turbulance)
        return max(odd_turbulance, even_turbulance)