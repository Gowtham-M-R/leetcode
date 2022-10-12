class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        count=0
        l = []
        for i in range(lo,hi+1):
            num=i
            while num != 1:
                if num%2 == 0:
                    num = num//2
                else:
                    num = 3 * num + 1
                count+=1
            l.append([count,i])
            count = 0
        l.sort()
        return l[k-1][1]