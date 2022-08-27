class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        if n == 1:
            return True
        if n%3 != 0:
            return False
        return self.isPowerOfThree(n/3)
        # while n>1:
        #     n=n/3
        # return n == 1