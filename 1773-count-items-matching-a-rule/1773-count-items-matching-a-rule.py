class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        l = ["type","color","name"]
        index = l.index(ruleKey)
        count = 0
        for i in items:
            if i[index] == ruleValue:
                count+=1
        return count