class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=[len(x) for x in strs]
        s=""
        m=strs[l.index(min(l))]
        print(m)
        for i in range(0,min(l)):
            count=0
            for j in strs:
                if j[i] == m[i]:
                    count+=1
                else:
                    break
            if count == len(strs):
                s = s + m[i]
            else:
                break
        return s