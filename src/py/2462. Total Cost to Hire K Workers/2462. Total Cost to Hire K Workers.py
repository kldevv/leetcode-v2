class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if k == len(costs):
            return sum(costs)
        
        min_heap = []
        n = len(costs)
        for i in range(candidates):
            heapq.heappush(min_heap, (costs[i], i))
            
        j = n-1
        for j in range(n-1, max(i, n-1-candidates), -1):
            heapq.heappush(min_heap, (costs[j], j))
        
        out = 0
        for kk in range(k):
            cost, idx = heapq.heappop(min_heap)
            out += cost
            # expand the border to include more candidates
            if i + 1 < j:
                if idx <= i:
                    i += 1
                    heapq.heappush(min_heap, (costs[i], i))
                else:
                    j -= 1
                    heapq.heappush(min_heap, (costs[j], j))
        return out
