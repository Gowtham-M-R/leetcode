class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l = []
        for i in sentences:
            s = i.split(" ")
            l.append(len(s))
        return max(l)