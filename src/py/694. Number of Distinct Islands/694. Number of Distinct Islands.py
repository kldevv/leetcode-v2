class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return "X"
            grid[i][j] = 0
            
            down = dfs(i+1, j)
            right = dfs(i, j+1)
            left = dfs(i, j-1)
            up = dfs(i-1, j)
            
            out = "$" + down + right + left + up
            return out
        
        islands = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    shape = dfs(i, j)
                    print(i, j, shape)
                    islands.add(shape)
                    
        return len(islands)