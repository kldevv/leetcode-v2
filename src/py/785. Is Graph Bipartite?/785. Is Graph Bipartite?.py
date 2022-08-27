class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [None] * len(graph)
        
        def dfs(u):
            for v in graph[u]:
                if colors[v] is not None and colors[v] == colors[u]:
                    return False
                
                if colors[v] is None:
                    colors[v] = 1 - colors[u]
                    if not dfs(v):
                        return False
            return True
        
        for u in range(len(graph)):
            if colors[u] is None:
                colors[u] = 0
                if not dfs(u):
                    return False
        return True
                
                
                