class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_dig(s):
            out = [0] * 2
            for c in s:
                out[c=="1"] += c == "1"
                out[c=="1"] += c == "0"
            return out
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zero, one = count_dig(s)
            for z in range(m, zero-1, -1):
                for o in range(n, one-1, -1):
                    dp[z][o] = max(dp[z][o], 1+dp[z-zero][o-one])
        return dp[m][n]

