class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def number(n):
            l = set(list(str(n)))
            if '0' in l:
                return False
            for i in l:
                if n % int(i) != 0:
                    return False
            return True
        r=[]
        for i in range(left,right+1):
            if number(i):
                r.append(i)
        return r
            