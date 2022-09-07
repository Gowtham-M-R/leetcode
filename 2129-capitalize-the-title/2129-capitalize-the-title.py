class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l = title.split()
        s = ''
        for i in l:
            if len(i) > 2:
                s+= i.capitalize()
                s += ' '
            else:
                s += i.lower()
                s += ' '
        return s[:len(s)-1]