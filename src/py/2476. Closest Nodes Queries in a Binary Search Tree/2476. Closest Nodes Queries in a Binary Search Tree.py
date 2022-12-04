# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        vals = []
        def traverse(root):
            if not root:
                return
            traverse(root.left)
            vals.append(root.val)
            traverse(root.right)
        traverse(root)
        
        n = len(vals)
        out = []
        for t in queries:
            i = bisect.bisect_left(vals, t)
            if i < n and vals[i] == t:
                out.append([t, t])
            elif i == n:
                out.append([vals[-1], -1])
            elif i == 0:
                out.append([-1, vals[0]])
            else:
                out.append([vals[i-1], vals[i]])
        return out
