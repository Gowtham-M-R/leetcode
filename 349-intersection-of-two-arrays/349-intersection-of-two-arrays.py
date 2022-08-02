class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
        # r=[]
        # for i in nums1:
        #     if i in nums2:
        #         if i not in r:
        #             r.append(i)
        # return r