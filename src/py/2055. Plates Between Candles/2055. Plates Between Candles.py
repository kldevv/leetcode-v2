class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        range_sum = [0] * n
        to_left = [0] * n
        to_right = [0] * n
        
        for i in range(n):
            if i > 0:
                range_sum[i] = range_sum[i-1] + int(s[i] == "*")
                to_left[i] = to_left[i-1] + 1 if s[i] == "*" else 0
            else:
                range_sum[i] = int(s[i] == "*")
                to_left[i] = int(s[i] == "*")
        
        for i in range(n-1, -1, -1):
            if i < n-1:
                to_right[i] = to_right[i+1] + 1 if s[i] == "*" else 0
            else:
                to_right[i] = int(s[i] == "*")
        
        out = []
        for start, end in queries:
            cnt = range_sum[end] - (range_sum[start-1] if start > 0 else 0)
            right_ex = to_right[start]
            left_ex = to_left[end]
            out.append(max(0, cnt - right_ex - left_ex))
        return out