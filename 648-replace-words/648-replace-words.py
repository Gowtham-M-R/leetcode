class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split(" ")
        for i in range(len(s)):
            for j in dictionary:
                if j == s[i][:len(j)]:
                    s[i]=j
        return " ".join(s)
            