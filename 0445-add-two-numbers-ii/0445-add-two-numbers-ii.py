# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1=None
        curr=l1
        while curr:
            nxt=curr.next
            curr.next=prev1
            prev1=curr
            curr=nxt
        prev2=None
        curr=l2
        while curr:
            nxt=curr.next
            curr.next=prev2
            prev2=curr
            curr=nxt
        dummy=ListNode(0)
        tail=dummy
        carry=0
        while prev1 or prev2 or carry:
            x=prev1.val if prev1 else 0
            y=prev2.val if prev2 else 0
            total=x+y+carry
            digit=total%10
            carry=total//10
            tail.next=ListNode(digit)
            tail=tail.next
            if prev1:
                prev1=prev1.next
            if prev2:
                prev2=prev2.next
        prev3=None
        curr=dummy.next
        while curr:
            nxt=curr.next
            curr.next=prev3
            prev3=curr
            curr=nxt
        return prev3
        