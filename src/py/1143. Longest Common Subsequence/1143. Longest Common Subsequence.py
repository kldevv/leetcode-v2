class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        
        if n < m:
            return self.longestCommonSubsequence(text2, text1)
        
        # m < n
        prev = [0] * (m + 1)
        for i in range(n-1, -1, -1):
            cur = [0] * (m + 1)
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = prev[j+1] + 1
                else:
                    cur[j] = max(cur[j+1], prev[j])
            prev = cur
        return cur[0]

