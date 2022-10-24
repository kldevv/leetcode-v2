class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo = 0
        hi = len(s)
        
        out = []
        for c in s:
            if c == "I":
                out.append(lo)
                lo += 1
            else:
                out.append(hi)
                hi -= 1
                
        return out + [hi]

