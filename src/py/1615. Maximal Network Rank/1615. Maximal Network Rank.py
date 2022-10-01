class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        roads_set = set()
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            roads_set.add((max(u, v), min(u, v)))
        
        max_rank = 0
        for u in range(n-1):
            for v in range(u+1, n):
                max_rank = max(max_rank, degree[u] + degree[v] - ((max(u, v), min(u, v)) in roads_set))
        
        return max_rank
        