class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        # dfs
        
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        restricted = set(restricted)
        visited = set()
        def dfs(node):
            if node in restricted:
                return 0
            
            visited.add(node)
            
            count = 1
            for neigh in graph[node]:
                if neigh not in visited:
                    count += dfs(neigh)
            
            return count
        
        return dfs(0)

