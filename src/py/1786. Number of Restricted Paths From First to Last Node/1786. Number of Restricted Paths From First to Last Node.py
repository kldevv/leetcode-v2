class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        weight = collections.defaultdict(list)
        for u, v, w in edges:
            weight[u-1].append([v-1, w])
            weight[v-1].append([u-1, w])
        
        def dijkstra():
            min_heap = [(0, n-1)]
            dist = {}
            while min_heap:
                w, u = heapq.heappop(min_heap)
                
                if u in dist:
                    continue
                    
                dist[u] = w
                for v, dw in weight[u]:
                    if v not in dist:
                        heapq.heappush(min_heap, [w+dw, v])
            return dist
                        
        dist = dijkstra()
        
        @lru_cache(None)
        def dfs(u=0):
            if u == n-1:
                return 1
            
            out = 0
            for v, w in weight[u]:
                if dist[u] > dist[v]:
                    out += dfs(v)
            return int(out % (1e9 + 7))
                    
        return dfs()
    