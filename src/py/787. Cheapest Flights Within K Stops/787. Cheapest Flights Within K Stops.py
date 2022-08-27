class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra's with most K stop
        
        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        
        found_optimal = set(f"{src},{k}")
        visited = set(str([0, src, k]))
        q = [[0, src, k]] # cost, node, k stops
        
        while q:
            cost, u, k = heapq.heappop(q)
            visited.add(f"{u},{k}")
            
            if u == dst:
                return cost
            
            if k >= 0:
                for v, w in graph[u].items():
                    cand = [cost+w, v, k-1]
                    if f"{v},{k-1}" not in found_optimal and str(cand) not in visited:
                        visited.add(str(cand))
                        heapq.heappush(q, cand)
        return -1
        
        