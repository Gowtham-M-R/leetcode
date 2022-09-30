class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        r,count = -1,-1
        for i in sorted(set(nums)):
            if i%2 ==0 and nums.count(i)>count:
                count = nums.count(i)
                r=i
        return r