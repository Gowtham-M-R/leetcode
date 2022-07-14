class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        i=0
        count=0
        if s == "":
            return True
        while i < len(s) and j < len(t):
            if s[i] not in t:
                return False
            if s[i]==t[j]:
                i+=1
                j+=1
                count+=1
                if count == len(s):
                    return True
            else:
                j+=1
        return False
                