class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Dijkstra's
        
        graph = [dict() for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u][v] = prob
            graph[v][u] = prob
        
        
        cand_routes = [(-1.0, start)]
        visited = set()
        
        while cand_routes:
            prob, node = heapq.heappop(cand_routes)
            visited.add(node)
            
            if node == end:
                return -prob
            
            for neigh, next_prob in graph[node].items():
                if neigh not in visited:
                    heapq.heappush(cand_routes, (next_prob*prob, neigh))
                    
        return 0

