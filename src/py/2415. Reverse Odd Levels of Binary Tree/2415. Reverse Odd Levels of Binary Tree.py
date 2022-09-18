# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_1 = [root]
        count = 0
        while level_1:
            count += 1
            level_2 = []
            for node in level_1:
                if node.left and node.right:
                    level_2 += [node.left, node.right]
            if count & 1 and level_2:
                level_2_val = [node.val for node in level_2]
                i = len(level_2_val) - 1
                for node in level_1:
                    node.left.val, node.right.val = level_2_val[i], level_2_val[i-1]
                    i -= 2
            level_1 = level_2
                
        return root
