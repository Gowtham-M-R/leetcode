class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = []
        for i in sentences:
            tl = i.split(" ")
            ans.append(len(tl))
        return max(ans)
