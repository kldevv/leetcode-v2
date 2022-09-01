class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # topological sort
        
        in_degrees = [0] * n
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            in_degrees[v] += 1
            graph[u].append(v)
        
        ancestors = [set() for _ in range(n)]
        p = [idx for idx, d in enumerate(in_degrees) if d == 0]
        
        for node in p:
            for neigh in graph[node]:
                ancestors[neigh] |= ancestors[node] | {node}
                in_degrees[neigh] -= 1
                if in_degrees[neigh] == 0:
                    p.append(neigh)
        
        return [sorted(list(s)) for s in ancestors]

