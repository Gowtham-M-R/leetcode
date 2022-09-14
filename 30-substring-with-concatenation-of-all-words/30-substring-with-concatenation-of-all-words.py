class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        w = len(words[0])
        k = len(words)
        l = w*k
        counter = collections.Counter(words)
        def check(i):
            remaining = counter.copy()
            used = 0
            for j in range(i,i+l,w):
                sub = s[j:j+w]
                if remaining[sub] > 0:
                    remaining[sub] -= 1
                    used += 1
                else:
                    break
            return used == k

        ans=[]
        for i in range((n-l)+1):
            if check(i):
                ans.append(i)
        return ans