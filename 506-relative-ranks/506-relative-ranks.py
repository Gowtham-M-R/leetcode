class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score)[::-1]
        i=0
        while i < len(score):
            num=s[i]
            index=score.index(num)
            if i == 0:
                score[index]="Gold Medal"
            elif i == 1:
                score[index]="Silver Medal"
            elif i == 2:
                score[index] = "Bronze Medal" 
            else:
                score[index] = str(i+1)
            i+=1
        return score