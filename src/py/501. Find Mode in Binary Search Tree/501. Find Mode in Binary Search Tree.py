# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_cnt = 0
        cur_val = 0
        cur_cnt = 0
        modes = None
        
        def process(val):
            nonlocal cur_val
            nonlocal cur_cnt
            nonlocal max_cnt
            
            if val != cur_val:
                cur_val = val
                cur_cnt = 0
            cur_cnt += 1
            
            max_cnt = max(max_cnt, cur_cnt)
            if cur_cnt == max_cnt and modes is not None:
                modes.append(val)
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            process(root.val)
            inorder(root.right)
        
        inorder(root)
        cur_cnt = 0
        modes = []
        inorder(root)
        return modes
        