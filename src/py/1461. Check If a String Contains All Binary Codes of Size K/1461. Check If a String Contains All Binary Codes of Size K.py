class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # to keep the interested bits
        mask = (1 << k) - 1
        visited = [0] * (mask + 1)
        cur_substr = 0
        
        for i, c in enumerate(s):
            cur_substr = ((cur_substr << 1) & mask) | int(c == '1')
            if i >= k - 1:
                visited[cur_substr] = 1
        
        return all(visited)