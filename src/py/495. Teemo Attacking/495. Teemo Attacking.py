class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        out = duration * n
        for i in range(1, n):
            offset = max(0, timeSeries[i-1] + duration - timeSeries[i])
            out -= offset
        return out
            
            