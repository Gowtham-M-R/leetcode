class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(map(str,digits))
        s=int(s)+1
        return [x for x in str(s)]
        