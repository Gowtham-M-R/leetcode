# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l,curr = [],head
        while curr:
            l.append(curr.val)
            curr = curr.next
        n = len(l)
        return max([a+b for a,b in zip(l[:n//2],l[n//2:][::-1])])