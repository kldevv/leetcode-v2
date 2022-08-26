class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # get adjacent graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        max_cost = 0
        visited = set()
        
        pq = [(0, k)]
        while pq:
            cost_from_k, u = heapq.heappop(pq)

            # we already found the shortest path to v before, given the properties of min heap
            if u in visited:
                continue
            visited.add(u)

            max_cost = max(max_cost, cost_from_k)

            for v, w in graph[u]:
                # we already found the shortest path to v before
                if v not in visited:
                    heapq.heappush(pq, (cost_from_k+w, v))


        return max_cost if len(visited) == n else -1
    