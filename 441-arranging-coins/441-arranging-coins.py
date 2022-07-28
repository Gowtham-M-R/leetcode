class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=1
        j=0
        while True:
            if n >= i:
                n-=i
                i+=1
                j+=1
            else:
                break
        return j