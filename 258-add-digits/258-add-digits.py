class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            n=0
            for i in str(num):
                n=n+int(i)
            if n < 10:
                break
            num=n
        return n
        