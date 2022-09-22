class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a,m = 0,1
        for i in str(n):
            a += int(i)
            m *= int(i)
        return m - a
            
            