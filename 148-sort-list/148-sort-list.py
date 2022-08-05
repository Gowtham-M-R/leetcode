# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        root=head
        root1=head
        while head:
            l+=[head.val]
            head=head.next
        l=sorted(l)
        i=0
        while root:
            root.val=l[i]
            root=root.next
            i+=1
        return root1