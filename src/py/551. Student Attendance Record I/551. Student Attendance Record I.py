class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        abs_cnt = 0
        for i in range(n):
            if i < n-2 and s[i] == s[i+1] == s[i+2] == "L":
                return False
            abs_cnt += (s[i] == "A")
        return abs_cnt < 2