class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bin_len = int(math.log(n) / math.log(2))
        mask = (1 << (bin_len + 1)) - 1
        return n ^ mask