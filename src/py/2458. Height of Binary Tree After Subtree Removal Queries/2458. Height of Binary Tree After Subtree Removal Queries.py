# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = defaultdict(int)
        
        def preorder(root, h):
            nonlocal cur_max_h
            if not root:
                return
            
            # max height to the left of the root vs height until parent
            heights[root.val] = max(heights[root.val], cur_max_h)
            cur_max_h = max(cur_max_h, h)
            
            preorder(root.left, h+1)            
            preorder(root.right, h+1)
        
        def preorder_rev(root, h):
            nonlocal cur_max_h
            if not root:
                return
            
            # max height to the right of the root vs height until parent
            heights[root.val] = max(heights[root.val], cur_max_h)
            cur_max_h = max(cur_max_h, h)
            
            preorder_rev(root.right, h+1)
            preorder_rev(root.left, h+1)          
            
        cur_max_h = 0
        preorder(root, 0)
        cur_max_h = 0
        preorder_rev(root, 0)
    
        
        out = []
        for q in queries:
            out.append(heights[q])
        return out
        