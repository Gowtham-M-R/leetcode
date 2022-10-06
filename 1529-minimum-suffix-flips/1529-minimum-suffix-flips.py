class Solution:
    def minFlips(self, target: str) -> int:
        c,count='0',0
        for i in target:
            if i == c:
                continue
            count+=1
            if c =='0':
                c='1'
            else:
                c='0'
        return count
            