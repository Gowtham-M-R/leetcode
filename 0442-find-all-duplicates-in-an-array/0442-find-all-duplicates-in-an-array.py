class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = set()
        r = set()
        for i in nums:
            if i not in l :
                l.add(i)
            else:
                r.add(i)
        return r