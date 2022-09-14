class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # tc(n): nlogn
        
        # min_heap
        itv_ends = []
        intervals.sort()
        
        for start, end in intervals:
            if len(itv_ends) and itv_ends[0] < start:
                heapq.heappop(itv_ends)
            heapq.heappush(itv_ends, end)
        
        return len(itv_ends)