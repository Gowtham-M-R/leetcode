class Solution:
    def capitalizeTitle(self, title: str) -> str:
        s=""
        for i in title.split(" "):
            if len(i) >= 3:
                s += i.capitalize()
            else:
                s+=i.lower()
            s+=" "
        return s[:len(title)]