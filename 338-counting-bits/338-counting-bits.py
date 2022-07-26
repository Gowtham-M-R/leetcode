class Solution:
    def countBits(self, n: int) -> List[int]:
        r=[]
        for i in range(n+1):
            l='{0:b}'.format(i)
            r.append(l.count('1'))
        return r
        
