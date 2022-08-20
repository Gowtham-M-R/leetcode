class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            a = nums[i]
            b = a + diff
            c = b + diff
            if b in nums and c in nums:
                count+=1
        return count