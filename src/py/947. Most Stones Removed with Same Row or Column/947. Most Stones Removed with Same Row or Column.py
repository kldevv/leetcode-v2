class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        K = 10001
        coords = defaultdict(list)
        for x, y in stones:
            coords[x].append(y+K)
            coords[y+K].append(x)
        
        def dfs(coord):
            visited.add(coord)
            for next_coord in coords[coord]:
                if next_coord not in visited:
                    dfs(next_coord)
            
        
        visited = set()
        components = 0
        for coord in coords.keys():
            if coord not in visited:
                components += 1
                dfs(coord)
        
        return len(stones) - components

