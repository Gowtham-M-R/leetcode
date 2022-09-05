class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=nums.index(max(nums))
        print(n)
        nums.sort()
        if nums[-2] * 2 <= nums[-1]:
            return n
        return -1