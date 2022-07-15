class Solution:
    def reverseWords(self, s: str) -> str:
        string=[]
        l=s.split(" ")
        for i in l:
            string.append(i[::-1])
        return " ".join(string)