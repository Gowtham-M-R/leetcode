class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = []
        n = 0
        for i in spaces:
            l.append(s[n:i])
            n = i
        l.append(s[n:])
        return " ".join(l)