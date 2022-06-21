class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=[s]
        l=' '.join(s).split()
        count=len(l[len(l)-1])
        return count
    