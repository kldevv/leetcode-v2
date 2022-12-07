class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        if not grid:
            return []
        
        n = len(grid)
        m = len(grid[0])
        
        rows = [0] * n
        cols = [0] * m

        for i in range(n):
            for j in range(m):
                # for i row, we only need onesRow_i - zeorsRow_i
                # so we can compress the counting into diff
                is_one = grid[i][j] == 1
                rows[i] += 1 if is_one else -1
                cols[j] += 1 if is_one else -1
        
        out = grid.copy()
        for i in range(n):
            for j in range(m):
                out[i][j] = rows[i] + cols[j]
        return out
