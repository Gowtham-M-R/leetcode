class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        l=[]
        for i in "balon":
            c=text.count(i)
            if i == 'l' or i == 'o':
                c=c//2
            l.append(c)
        return min(l)
        
        
        # return min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n'))