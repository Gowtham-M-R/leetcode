class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = list(set(nums))
        n1=[nums.count(x) for x in n]
        m = max(n1)
        return n[n1.index(m)]
            