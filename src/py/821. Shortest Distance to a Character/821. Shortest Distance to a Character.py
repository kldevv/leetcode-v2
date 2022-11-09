class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        out = [n] * n
        
        cur_dist = n
        for i, t in enumerate(s):
            if t == c:
                cur_dist = 0
            else:
                cur_dist += 1
            out[i] = cur_dist
        
        cur_dist = n
        for i in range(n-1, -1, -1):
            if s[i] == c:
                cur_dist = 0
            else:
                cur_dist += 1
            out[i] = min(out[i], cur_dist)
        
        return out