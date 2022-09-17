class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        for i in range(len(sentences)):
            n = len(sentences[i].split())
            sentences[i] = n
        return max(sentences)