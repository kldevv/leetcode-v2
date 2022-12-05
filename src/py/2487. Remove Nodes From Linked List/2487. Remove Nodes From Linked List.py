# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        # reverse linked list
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            
        node = prev
        prev = None
        out = None
        max_val = -1
        while node:
            if node.val >= max_val:
                max_val = node.val
                out = ListNode(node.val, out)
            # reverse link list
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return out
