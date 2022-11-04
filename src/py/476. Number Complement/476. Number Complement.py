class Solution:
    def findComplement(self, num: int) -> int:
        bin_len = int(math.log(num) / math.log(2))
        mask = (1 << (bin_len + 1)) - 1
        return num ^ mask

