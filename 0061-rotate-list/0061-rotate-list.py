# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        curr=head
        c=1
        while curr.next:
            c+=1
            curr=curr.next
        curr.next=head
        k=k%c
        if k==0:
            curr.next=None
            return head
        val=c-k-1
        new_tail=head
        for i in range(val):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head


