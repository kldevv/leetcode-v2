"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def flatten_dfs(head):
            # returns tail of the flatten array
            cur_tail = None
            while head:
                if head.child:
                    tail = flatten_dfs(head.child)
                    head.child.prev = head
                    if head.next:
                        head.next.prev = tail
                    head.next, tail.next = head.child, head.next
                head.child = None
                cur_tail = head
                head = head.next
            return cur_tail
        
        flatten_dfs(head)
        
        return head

