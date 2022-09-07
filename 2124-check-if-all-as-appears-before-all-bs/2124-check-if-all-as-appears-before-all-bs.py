class Solution:
    def checkString(self, s: str) -> bool:
        srtd = sorted(s)
        return "".join(srtd) == s