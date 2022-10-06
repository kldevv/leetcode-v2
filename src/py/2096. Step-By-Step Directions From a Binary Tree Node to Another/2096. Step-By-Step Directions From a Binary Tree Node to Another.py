# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find(root, target, path):
            if root.val == target:
                return path
            
            if root.left:
                path.append("L")
                left_find = find(root.left, target, path)
                if left_find:
                    return left_find
                path.pop()
            
            if root.right:
                path.append("R")
                right_find = find(root.right, target, path)
                if right_find:
                    return right_find
                path.pop()
            
        path_to_start = find(root, startValue, [])
        path_to_dest = find(root, destValue, [])
        
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1
        
        return "U" * (len(path_to_start) - i) + "".join(path_to_dest[i:])
                