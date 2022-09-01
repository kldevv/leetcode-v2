class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # topological sort
        
        n = len(graph)
        
        re_graph = [set() for _ in range(n)]
        out_degrees = [len(graph[node]) for node in range(n)]
        
        q = []
        
        for node in range(n):
            if len(graph[node]) == 0:
                q.append(node)
            for neigh in graph[node]:
                re_graph[neigh].add(node)
        
        safe_nodes = []
        while q:
            safe_node = q.pop()
            safe_nodes.append(safe_node)
            
            for neigh in re_graph[safe_node]:
                out_degrees[neigh] -= 1
                if out_degrees[neigh] == 0:
                    q.append(neigh)
        
        return sorted(safe_nodes)
            