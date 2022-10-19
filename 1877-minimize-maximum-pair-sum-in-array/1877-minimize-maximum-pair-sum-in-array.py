class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        result = []
        nums.sort()
        for i in range(len(nums)//2):
            result.append(nums[i]+nums[len(nums)-1-i])
        return max(result)