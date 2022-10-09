class Solution:
    def maxPower(self, s: str) -> int:
        r = 1
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count+=1
                r = max(r,count)
            else:
                count=1
        return r