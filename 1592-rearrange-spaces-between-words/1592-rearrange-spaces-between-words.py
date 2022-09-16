class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = ""
        t = text
        space = text.count(" ")
        text = text.split()
        if len(text) == 1:
            return "".join(text)+ space * " "
        l = space // (len(text)-1)
        rem = space % (len(text)-1)
        return (' ' * l).join(text) + (rem * " ")