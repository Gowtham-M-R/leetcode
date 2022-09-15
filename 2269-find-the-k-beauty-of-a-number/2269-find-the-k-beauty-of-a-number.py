class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        l = len(s)
        count = 0
        for i in range(l-k+1):
            n = int(s[i:i+k])
            if n !=0 and num % n == 0 :
                count+=1
        return count