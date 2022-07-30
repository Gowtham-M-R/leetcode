class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s=""
        r=[]
        for i in range(len(words)):
            for j in words[i]:
                s=s+l[ord(j)-97]
            if s not in r:
                r.append(s)
            s=""
        return len(r)
            
            
 