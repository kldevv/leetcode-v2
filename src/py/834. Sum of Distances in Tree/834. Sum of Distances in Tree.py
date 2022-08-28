class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        counts = [1] * n
        results = [0] * n
        
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    counts[node] += counts[child]
                    # all nodes dis to cur_node is all nodes dis to all cur_node's child plus how many descendant the child have (each descendant contribute 1 dis)
                    results[node] += counts[child] + results[child]
        # first calculate all nodes dis to root
        dfs(0, None)
        
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    # divide dis to node
                    # dis to child is minus one for all descendant on child's subtree
                    # and plus one for all descendant not on child's subtree
                    results[child] = results[node] - counts[child] + (n - counts[child])
                    dfs2(child, node)
                    
        dfs2(0, None)
        
        return results