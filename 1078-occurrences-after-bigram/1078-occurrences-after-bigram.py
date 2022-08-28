class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l=[]
        text=text.split(' ')
        for i in range(len(text)-2):
            if first == text[i] and second == text[i+1]:
                l.append(text[i+2])
        return l
        
                