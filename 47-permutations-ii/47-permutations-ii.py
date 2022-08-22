class Solution: 
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=list(itertools.permutations(nums))
        for i in l:
            i=list(i)
        return set(l)
        