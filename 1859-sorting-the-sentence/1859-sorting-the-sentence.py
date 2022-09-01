class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split(" ")
        a.sort(key=lambda x:x[-1])
        a = [i[:-1]for i in a ]
        return " ".join(a)