class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s=[]
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if words[j] != words[i] and words[j] not in s:
                    if words[j] in words[i]:
                        s.append(words[j])
                    if words[i] in words[j]:
                        s.append(words[i])
        return set(s)