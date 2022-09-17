# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = {}
        def flatten(node):
            if node:
                out = str(node.val) + "/" + str(flatten(node.left)) + "/" + str(flatten(node.right))
                if out not in seen:
                    seen[out] = [node, 0]
                seen[out][1] += 1
                return out
        
        flatten(root)
        
        return [node for node, count in seen.values() if count > 1]

