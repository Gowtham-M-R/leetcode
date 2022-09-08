class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        l=[]
        while i < len(s):
            if i < len(s)-2 and s[i+2] == '#':
                l.append(s[i:i+2])
                print(i,"hello")
                i+=2
            else:
                l.append(s[i])
            i+=1
        return "".join([chr(int(i)+96) for i in l])