# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l_d=ListNode(0)
        s_d=ListNode(0)
        s=s_d
        l=l_d
        while head:
            if head.val>=x:
                l.next=head
                l=l.next
            else:
                s.next=head
                s=s.next
            head=head.next
        l.next=None
        s.next=l_d.next
        return s_d.next