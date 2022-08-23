class Solution:
    def dayOfYear(self, date: str) -> int:
        y = int(date[:4])
        m = int(date[5:7])
        d = int(date[8:])
        s = 0
        mon = [31,28,31,30,31,30,31,31,30,31,30,31]
        if m == 1:
            return d
        def isleap(y):
            if (y%4 == 0 and y%100 != 0) or y%400 == 0:
                mon[1]+=1
        isleap(y)
        for i in range(m-1):
            s += mon[i]
        return s + d
            