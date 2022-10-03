class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cur_sum = 0
        max_sum = 0
        for i in range(1, m-1):
            cur_sum = grid[i][1] + sum(grid[i-1][:3]) + sum(grid[i+1][:3])
            max_sum = max(max_sum, cur_sum)
            for j in range(2, n-1):
                cur_sum -= (grid[i][j-1] + grid[i-1][j-2] + grid[i+1][j-2])
                cur_sum += (grid[i][j] + grid[i-1][j+1] + grid[i+1][j+1])
                max_sum = max(max_sum, cur_sum)
        return max_sum