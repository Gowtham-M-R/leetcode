class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count=0
        for i in text.split(" "):
            if len(set(i).intersection(brokenLetters)) == 0:
                count+=1
        return count
    