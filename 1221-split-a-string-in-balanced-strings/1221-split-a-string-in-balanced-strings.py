class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r,l,count = 0,0,0
        for i in s:
            if i == "R":
                r+=1
            if i == "L":
                l+=1
            if r == l :
                count+=1
                r,l = 0,0
        return count
                    