class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l=[]
        i,j=0,1
        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                j+=1
            else:
                if j-i>=3:
                    l.append([i,j-1])
                i = j
        if j-i>=3:
            l.append([i,j-1])
        return l
                    
        