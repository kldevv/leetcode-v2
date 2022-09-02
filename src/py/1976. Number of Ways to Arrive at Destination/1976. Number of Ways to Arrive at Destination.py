class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Dijkstra's
        
        MOD = pow(10, 9) + 7
        
        graph = [dict() for _ in range(n)]
        for u, v, dist in roads:
            graph[u][v] = dist
            graph[v][u] = dist
        
        optimal_dist = [float('inf')] * n
        optimal_dist[0] = 0
        
        optimal_way_counts = [0] * n
        optimal_way_counts[0] = 1
        
        minHeap = [(0, 0)]
        
        while minHeap:
            accu_dist, node = heapq.heappop(minHeap)
            
            # because minHeap sort distance then node index
            # same distance, node index smaller will be popped first
            # thus, upon popping node, optimal_dist[node] and optimal_way_counts[node] are always final
            if node == n-1:
                return optimal_way_counts[n-1]
                
            for neigh, dist in graph[node].items():
                cand_time = accu_dist + dist
                # upon reaching node+1, optimal_dist[node] and optimal_way_counts[node] are always final
                if optimal_dist[neigh] > cand_time:
                    optimal_way_counts[neigh] = optimal_way_counts[node]
                    optimal_dist[neigh] = cand_time
                    heapq.heappush(minHeap, (optimal_dist[neigh], neigh))
                elif optimal_dist[neigh] == cand_time:
                    optimal_way_counts[neigh] = (optimal_way_counts[node] + optimal_way_counts[neigh]) % MOD
                    # notice that we're not pushing neigh again, because it's already in queue
                    # just need to update the count
                    
        return optimal_way_counts[n-1]