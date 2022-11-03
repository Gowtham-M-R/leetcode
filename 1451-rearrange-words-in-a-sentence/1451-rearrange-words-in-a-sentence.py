class Solution:
    def arrangeWords(self, text: str) -> str:
        t = list(text.split())
        return " ".join(sorted(t,key = len)).capitalize()
            
            