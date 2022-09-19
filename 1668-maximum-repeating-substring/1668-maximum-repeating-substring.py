class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 1
        while (count*word in sequence):
            count+=1
        return count-1