class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        current = nums.copy()
        for i in current:
            nums.append(int(str(i)[::-1]))
        return len(set(nums))