class Solution:
    def minimumDeletions(self, s: str) -> int:
        out = 0
        b_cnt = 0
        for c in s:
            if c == "a":
                out = min(out+1, b_cnt)
            else:
                b_cnt += 1
        return out