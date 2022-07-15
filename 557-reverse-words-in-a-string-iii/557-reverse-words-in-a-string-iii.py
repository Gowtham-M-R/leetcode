class Solution:
    def reverseWords(self, s: str) -> str:
        string=""
        for i in s.split(" "):
            string+=i[::-1]+" "
        return string[0:len(s)]