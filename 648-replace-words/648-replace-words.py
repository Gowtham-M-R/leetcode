class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=sentence.split(" ")
        for i in range(len(s)):
            for j in range(len(dictionary)):
                if dictionary[j] == s[i][:len(dictionary[j])]:
                    s[i]=dictionary[j]
        return " ".join(s)
            