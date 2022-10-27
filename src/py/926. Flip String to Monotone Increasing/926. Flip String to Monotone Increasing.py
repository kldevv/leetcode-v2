class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        out = 0
        prev_1 = 0
        for c in s:
            if c == "0":
                # keep 1, remove all prev 1
                # drop 1, out_{i} = out_{i-1} +1
                out = min(out+1, prev_1)
            else:
                prev_1 += 1
        return out

