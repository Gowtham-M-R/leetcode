class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a,b=0,len(s)
        l=[]
        for i in s:
            if i == "I":
                l.append(a)
                a+=1
            elif i == "D":
                l.append(b)
                b-=1
        l.append(a)
        return l