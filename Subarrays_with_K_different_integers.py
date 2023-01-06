class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        #Exactly K = atmost K- atmost K-1
        return self.atmostk(nums,k)-self.atmostk(nums,k-1)

    def atmostk(self,nums,k):
        hash={}
        start,end=0,0
        count=0
        while end<len(nums):
            if nums[end] in hash:
                hash[nums[end]]+=1
            else:
                hash.update({nums[end]:1})
            while len(hash)>k: #exceeded #of distinct elm ,k=2
                hash[nums[start]]-=1
                if hash[nums[start]]==0:
                    del hash[nums[start]]
                start+=1

            count+=end-start+1
            end+=1
        
        return count