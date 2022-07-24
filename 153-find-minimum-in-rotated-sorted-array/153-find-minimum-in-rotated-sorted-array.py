class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=1
        m=nums[0]
        while i<len(nums):
            if nums[i]<m:
                m=nums[i]
            i+=1
        return m