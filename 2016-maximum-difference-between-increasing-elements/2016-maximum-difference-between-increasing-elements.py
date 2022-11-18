class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                m = max(nums[j]-nums[i],m)
        if m == 0:
            return -1
        return m