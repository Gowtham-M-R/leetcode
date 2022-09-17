class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [x for x in nums if x>0]
        neg = [y for y in nums if y<0]
        res = zip(pos,neg)
        return chain(*res)