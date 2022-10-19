class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        
        o, z, oz, zo, out = 0, 0, 0, 0, 0
        
        for i in range(n):
            if s[i] == "1":
                out += oz
                zo += z
                o += 1
            else:
                out += zo
                oz += o
                z += 1
                
        return out 
#         dp = [[1] + [0] * 3 for _ in range(2)]
        
#         for i in range(n):
#             for k in range(3, 0, -1):
#                 dp[int(s[i])][k] += dp[(int(s[i]) + 1) % 2][k-1]
#         return dp[0][3] + dp[1][3]