class Solution:
    def checkString(self, s: str) -> bool:
        s1 = sorted(s)
        return "".join(s1) == s