class Solution:
    def partitionString(self, s: str) -> int:
        t=""
        count = 0
        for i in s:
            if i not in t:
                t+=i
            else:
                count+=1
                t = "" +i
        return count+1