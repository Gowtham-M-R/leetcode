class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        li=[]
        s=""
        for i in key:
            if i == " " or i in li:
                continue
            li.append(i)
        for j in message:
            if j == " ":
                s = s + " "
            else:
                s = s + chr(97+li.index(j))
        return s
                