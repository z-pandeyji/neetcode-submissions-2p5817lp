"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        mapping = {}

        curr = head
        while curr is not None:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr is not None:
            if curr.next is not None:
                mapping[curr].next = mapping[curr.next]
            else:
                mapping[curr].next = None
            if curr.random is not None:
                mapping[curr].random = mapping[curr.random]
            else:
                mapping[curr].random = None
            
            curr = curr.next

        return mapping[head]
        