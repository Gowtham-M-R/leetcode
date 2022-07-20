class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = nums[0]
        cnt = 1
        
        for i in range (1,len(nums)):
            if nums[i]>tmp :
                tmp = nums[i]
                nums[cnt] = tmp
                cnt+=1
                
        return cnt