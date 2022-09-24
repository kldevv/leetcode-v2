class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        count = [n for _ in range(256)]
        
        for i, c in enumerate(s):
            if count[ord(c)] == n:
                count[ord(c)] = i
            else:
                count[ord(c)] = n + 1
        out = min(count)
        return out if out != n else -1
