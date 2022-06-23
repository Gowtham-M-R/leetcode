class Solution:
    def reverse(self, x: int) -> int:
        n=-2**31
        n1=2**31-1
        l=list(str(x)[::-1])
        if l[-1] == '-':
            l.pop()
            l.insert(0,'-')
        s=int(''.join(l))
        if s<n or n1<s:
            return 0
        return s
        
        