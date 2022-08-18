class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=set()
        l=0
        for i in range(len(nums)):
            if nums[i] in n:
                return True
            n.add(nums[i])
            if i >= k:
                n.remove(nums[l])
                l+=1
        return False