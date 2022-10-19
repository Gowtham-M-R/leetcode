class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        current = set(nums)
        new = set()
        for i in current:
            s = int(str(i)[::-1])
            if s not in current:
                new.add(s)
        return len(current)+len(new)