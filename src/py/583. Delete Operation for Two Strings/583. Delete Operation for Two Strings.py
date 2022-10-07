class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # longest common subsequence
        # can be improve by making the array 1-D
        
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        lcs_len = 0
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    lcs_len = max(lcs_len, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                    
        return n + m - lcs_len * 2

