class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # traversing connected component of 1

        graph = defaultdict(dict)
        for a, b, dist in roads:
            graph[a][b] = dist
            graph[b][a] = dist

        q = deque([1])
        # we don't pre-cache 1, because the min path might pass through 1
        vis = set()
        out = inf
        while q:
            cur_city = q.popleft()

            for adj_city, dist in graph[cur_city].items():
                if adj_city not in vis:
                    vis.add(adj_city)
                    q.append(adj_city)
                # for all paths to adj_city T, we count the path with the min score
                out = min(dist, out)
        
        return out
  