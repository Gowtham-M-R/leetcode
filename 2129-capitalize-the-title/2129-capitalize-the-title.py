class Solution:
    def capitalizeTitle(self, title: str) -> str:
        t=title.split()
        s=""
        for i in t:
            if len(i) > 2:
                s += i.capitalize()
            else:
                s+=i.lower()
            s+=" "
        return s[:len(title)]