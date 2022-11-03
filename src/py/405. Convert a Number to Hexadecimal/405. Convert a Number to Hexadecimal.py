class Solution:
    def toHex(self, num: int) -> str:
        converter = {i: str(i) for i in range(10)} | {j: chr(ord('a') + j - 10) for j in range(10, 16)}
        base = 16
        
        if num < 0:
            num = ((1 << 32) + num)
        out = []
        while num:
            out.append(converter[num % base])
            num //= base
        return "".join(out[::-1] or ["0"])

