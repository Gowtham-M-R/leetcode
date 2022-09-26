class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = [0]*len(names)
        h = heights.copy()
        h.sort(reverse=True)
        for i in range(len(h)):
            s = heights.index(h[i])
            l.insert(i,names[s])
        return l[:len(h)]