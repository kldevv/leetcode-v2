class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_timestamp(hour, minute):
            return hour * 60 + minute
        
        all_times = []
        visited = set()
        for time in timePoints:
            hour, minute = [int(x) for x in time.split(":")]
            if (hour, minute) in visited:
                return 0
            visited.add((hour, minute))
            all_times.append(get_timestamp(hour, minute))
        
        all_times.sort()
        all_times.append(all_times[0] + 24 * 60)
        
        min_diff = 24 * 60
        for i in range(1, len(all_times)):
            min_diff = min(min_diff, all_times[i] - all_times[i-1])
        return min_diff
            
        