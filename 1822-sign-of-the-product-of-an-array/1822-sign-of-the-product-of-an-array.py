class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for i in nums:
            if i == 0:
                return 0
            elif i > 0:
                s*=1
            else:
                s*=-1
        return s