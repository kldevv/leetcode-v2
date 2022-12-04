# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swap_to_sort(arr):
            pos = {x:i for i, x in enumerate(arr)}
            s_arr = sorted(arr)
            out = 0
            for a, b in zip(arr, s_arr):
                if a != b:
                    out += 1
                    arr[pos[a]], arr[pos[b]] = b, a
                    pos[a], pos[b] = pos[b], pos[a]
            return out
        
        q = [root]
        out = 0
        while q:
            out += min_swap_to_sort([node.val for node in q])
            
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return out