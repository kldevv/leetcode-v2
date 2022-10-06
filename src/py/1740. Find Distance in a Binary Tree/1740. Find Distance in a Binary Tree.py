# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p == q:
            return 0
        
        def find(root, target, path):
            if root.val == target:
                return True
            
            if root.left:
                path.append(0)
                find_left = find(root.left, target, path)
                if find_left:
                    return True
                path.pop()
                
            if root.right:
                path.append(1)
                find_right = find(root.right, target, path)
                if find_right:
                    return True
                path.pop()
        
        p_path = []
        find(root, p, p_path)
        p_n = len(p_path)
        
        q_path = []
        find(root, q, q_path)
        q_n = len(q_path)
        
        i = 0
        while i < p_n and i < q_n and p_path[i] == q_path[i]:
            i += 1
            
        return p_n + q_n - i * 2

