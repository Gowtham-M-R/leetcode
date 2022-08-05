# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        root=root1=head
        while head:
            l+=[head.val]
            head=head.next
        for i in range(1, len(l)):
            j = i-1
            key = l[i]
            while (j >= 0) and (l[j] > key):
                l[j+1] = l[j]
                j -= 1
            l[j+1] = key
        k=0
        while root:
            root.val=l[k]
            root=root.next
            k+=1
        return root1