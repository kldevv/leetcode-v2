class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        out = []
        for digit in num:
            while k and out and out[-1] > digit:
                out.pop()
                k -= 1
            out.append(digit)
        
        if k:
            out = out[:-k]
        return "".join(out).lstrip("0") or "0"
            