class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_diff = []
        
        out = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                diff = heights[i] - heights[i-1]
                heapq.heappush(min_diff, diff)
                
                if len(min_diff) > ladders:
                    bricks -= heapq.heappop(min_diff)
                    if bricks < 0:
                        break
            out += 1
        return out

