class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = sorted(nums[1::2],reverse = True)
        even = sorted(nums[::2])
        l = []
        for i in range(len(nums)):
            if i%2 == 0:
                l.append(even[i//2])
            else:
                l.append(odd[i//2])
        return l