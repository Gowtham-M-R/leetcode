class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=nums[0]
        c=1
        for i in range(1,len(nums)):
            if nums[i]>s:
                s=nums[i]
                nums[c]=s
                c+=1
        return c