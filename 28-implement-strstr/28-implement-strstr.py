class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if needle == haystack[i:i+n]:    
                return i