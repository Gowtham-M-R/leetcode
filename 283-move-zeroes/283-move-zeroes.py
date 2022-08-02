class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,c=0,0
        while c<len(nums):
            if nums[i]==0:
                nums.append(nums[i])
                nums.pop(i)
            else:
                i+=1
            c+=1
        return nums