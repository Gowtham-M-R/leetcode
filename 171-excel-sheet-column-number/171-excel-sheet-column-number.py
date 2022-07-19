class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s=0
        for i in columnTitle:
            s=s*26+(ord(i)-64)
        return s