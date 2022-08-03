class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        return max(c,key=c.get)