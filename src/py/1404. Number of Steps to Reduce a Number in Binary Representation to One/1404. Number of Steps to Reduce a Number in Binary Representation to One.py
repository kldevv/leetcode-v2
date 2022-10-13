class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        for c in s:
            num <<= 1
            num |= int(c == "1")
        
        out = 0
        while num != 1:
            out += 1
            if num & 1:
                num += 1
            else:
                num >>= 1
        return out

