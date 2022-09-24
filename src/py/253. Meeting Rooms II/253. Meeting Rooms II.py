class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []
        rooms = 0
        
        for start, end in intervals:
            while min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
            rooms = max(len(min_heap), rooms)
        return rooms

