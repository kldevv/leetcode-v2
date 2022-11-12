class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # tc(n) = n * target * k
        
        M = int(10 ** 9 + 7)
        
        @lru_cache(None)
        def dp(n, k, target):
            # print(n, target)
            if n == 1:
                return int(target <= k)
            
            out = 0
            for j in range(1, k+1):
                if target - j > 0:
                    out = (out + dp(n-1, k, target-j)) % M
            return out
    
        return dp(n, k, target)
