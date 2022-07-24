class Solution:
    def reverseWords(self, s: str) -> str:
        s1=""
        for i in s.split()[::-1]:
            s1+=i+" "
        return s1[:len(s1)-1]