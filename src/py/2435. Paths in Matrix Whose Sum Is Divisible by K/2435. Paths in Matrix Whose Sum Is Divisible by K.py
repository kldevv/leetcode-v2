class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD_FACTOR = int(10**9 + 7)
        n = len(grid)
        m = len(grid[0])
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(n):
            for j in range(m):                
                for kk in range(k):
                    trans = (kk + grid[i][j]) % k
                    if i > 0:
                        dp[i][j][trans] += dp[i-1][j][kk] 
                    if j > 0:
                        dp[i][j][trans] += dp[i][j-1][kk]
        return dp[n-1][m-1][0] % MOD_FACTOR

