class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = Counter(arr)
        num = sorted(l.values() ,reverse = True)
        i = 0
        h = len(arr)/2
        while h>0:
            h -= num[i]
            i+=1
        return i