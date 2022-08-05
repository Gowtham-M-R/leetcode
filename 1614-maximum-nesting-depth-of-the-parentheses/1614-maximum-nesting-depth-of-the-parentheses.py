class Solution:
    def maxDepth(self, s: str) -> int:
        count,a=0,0
        for i in s:
            if i == "(":
                count+=1
            elif i == ")":
                count-=1
            a=max(a,count)
        return a