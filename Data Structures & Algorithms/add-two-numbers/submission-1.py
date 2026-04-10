# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        p1 = l1
        p2 = l2
        carry = 0

        while p1 is not None or p2 is not None or carry != 0:
            if p1 is not None:
                val1 = p1.val
            else:
                val1 = 0
            if p2 is not None:
                val2 = p2.val
            else:
                val2 = 0
            
            total = val1 + val2 + carry
            digits = total % 10
            carry = total // 10

            tail.next = ListNode(digits)
            tail = tail.next

            if p1 is not None:
                p1 = p1.next
            if p2 is not None:
                p2 = p2.next

        return dummy.next
        