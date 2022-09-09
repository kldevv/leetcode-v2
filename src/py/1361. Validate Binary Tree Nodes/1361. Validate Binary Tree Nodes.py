class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        in_degree = [0] * n
        children = [set() for _ in range(n)]
        
        for idx, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                in_degree[left] += 1
                children[idx].add(left)
            if right != -1:
                in_degree[right] += 1
                children[idx].add(right)
                
            # A tree node can have at most 1 in-degree, otherwise cycle
            if in_degree[left] > 1 or in_degree[right] > 1:
                return False
            
        
        root = -1
        for idx, degree in enumerate(in_degree):
            if degree == 0:
                # Multiple roots found
                if root != -1:
                    return False
                root = idx
        
        # No root found
        if root == -1:
            return False
        
        # See if all the nodes are reachable from the root
        def dfs(node):
            out = 1
            for child in children[node]:
                out += dfs(child)
            return out
        
        return dfs(root) == n
