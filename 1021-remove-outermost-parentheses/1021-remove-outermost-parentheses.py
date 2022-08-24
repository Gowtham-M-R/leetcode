class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r = ""
        b = 0
        for i in s:
            if i == '(':
                b+=1
                if b > 1:
                    r+='('
            else:
                if b > 1:
                    r+=')'
                b-=1
        return r