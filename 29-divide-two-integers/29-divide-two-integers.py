class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        n=(2**31)-1
        n1=-(2**31)
        n2=int(dividend/divisor)
        if n2>n:
            return n
        elif n2<n1:
            return n1
        else:
            return n2