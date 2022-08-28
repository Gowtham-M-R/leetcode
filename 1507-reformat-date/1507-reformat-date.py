class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split(" ")
        d = date[0]
        d = d[:len(d)-2]
        m = month.index(date[1])+1
        y = date[2]
        if int(d) < 10:
            d = '0' + d
        if m < 10:
            m = '0' + str(m)
        return (f'{y}-{m}-{d}')