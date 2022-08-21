class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        d=dict()
        t=""
        for i in range(len(s)):
            if s[i].isalpha():
                t+=s[i]
            else:
                d[i]=s[i]
        t=t[::-1]
        r=[x for x in t]
        for j in d:
            r.insert(j,d[j])
        return "".join(r)