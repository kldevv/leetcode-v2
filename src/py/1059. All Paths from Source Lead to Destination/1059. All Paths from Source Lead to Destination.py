class Solution:
    VISITING = 1
    VISITED = 0
    
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        
        def dfs(node, dest, graph, states) -> bool:
            if len(graph[node]) == 0:
                return node == dest
            
            if states[node] is not None:
                return states[node] == Solution.VISITED
            
            # Note that we cache the visited node, if the node is visited and the programming is still running, we know that dfs starting from such node will yield valid result
            states[node] = Solution.VISITING
            for next_node in graph[node]:
                if not dfs(next_node, dest, graph, states):
                    return False
            states[node] = Solution.VISITED
            
            return True
        
        return dfs(source, destination, graph, [None] * n)
