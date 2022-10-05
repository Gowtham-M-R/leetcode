class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        s=[]
        y = nums[n:]
        for i in zip(x,y):
            s+=i
        return s