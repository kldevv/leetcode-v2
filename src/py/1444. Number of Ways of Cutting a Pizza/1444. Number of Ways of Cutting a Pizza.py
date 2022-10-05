class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        APPLE = "A"
        MOD_FACTOR = int(10 ** 9 + 7)
        n = len(pizza)
        m = len(pizza[0])
        matrix_sum_rl = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                matrix_sum_rl[i][j] = matrix_sum_rl[i+1][j] + matrix_sum_rl[i][j+1] \
                    - matrix_sum_rl[i+1][j+1] + int(pizza[i][j] == APPLE)
        
        @lru_cache(None)
        def dfs(i, j, k):
            if matrix_sum_rl[i][j] == 0:
                return 0
            if k == 0:
                return 1
            
            cur_sum = matrix_sum_rl[i][j]
            out = 0
            for next_i in range(i+1, n):
                if cur_sum - matrix_sum_rl[next_i][j]:
                    out = (out + dfs(next_i, j, k-1)) % MOD_FACTOR

            for next_j in range(j+1, m):
                if cur_sum - matrix_sum_rl[i][next_j]:
                    out = (out + dfs(i, next_j, k-1)) % MOD_FACTOR
            return out
        
        return dfs(0, 0, k-1)
            
            