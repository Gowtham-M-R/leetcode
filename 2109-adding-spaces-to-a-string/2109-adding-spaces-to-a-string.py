class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        l = []
        n = spaces[0]
        l.append(s[:n])
        for i in range(1,len(spaces)):
            l.append(s[n:spaces[i]])
            n = spaces[i]
        l.append(s[n:])
        return " ".join(l)