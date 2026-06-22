# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lo=ListNode(0)
        le=ListNode(0)
        l1=lo
        l2=le
        c=1
        while head:
            if c%2==0:
                l2.next=head
                l2=l2.next
            else:
                l1.next=head
                l1=l1.next
            c+=1
            head=head.next
        l2.next=None
        l1.next=le.next
        return lo.next