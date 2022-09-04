class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s=[]
        for i in range(0,len(words)):
            for j in range(0,len(words)):
                if words[j] != words[i] and words[j] not in s:
                    if words[j] in words[i]:
                        s.append(words[j])
        return s