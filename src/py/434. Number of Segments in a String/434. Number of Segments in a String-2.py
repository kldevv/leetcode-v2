class Solution:
    def countSegments(self, s: str) -> int:
        i = 0
        out = 0
        while i < len(s):
            try:
                next_i = s.index(" ", i)
            except:
                next_i = len(s)
            out += (next_i - i > 0)
            i = next_i + 1
        return out