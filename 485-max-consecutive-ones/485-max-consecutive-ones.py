class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans,count=0,0
        l=[]
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                ans=max(ans,count)
                count=0
        ans=max(ans,count)
        return ans
                