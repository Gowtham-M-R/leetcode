class Solution:
    def fib(self, n: int) -> int:
        l=[0,1,1]
        for i in range(2,n):
            s=l[i]+l[i-1]
            l.append(s)
        return l[n]