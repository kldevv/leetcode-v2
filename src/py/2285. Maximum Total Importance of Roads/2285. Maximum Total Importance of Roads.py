class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        city_road_counts = [0] * n
        
        for c1, c2 in roads:
            city_road_counts[c1] += 1
            city_road_counts[c2] += 1
            
        city_road_counts.sort()
        
        importants = 0
        for i in range(n):
            # important of the city times bound road count is the total important to contribute
            importants += city_road_counts[i] * (i + 1)
            
        return importants
