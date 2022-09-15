class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s = str(num)
        count = 0
        for i in range(len(s)-k+1):
            n = int(s[i:i+k])
            if n == 0:
                continue
            if num % n == 0 :
                count+=1
        return count