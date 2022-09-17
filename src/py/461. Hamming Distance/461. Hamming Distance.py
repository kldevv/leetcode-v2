class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        def count_bits(num):
            count = 0
            while num:
                num &= (num - 1)
                count += 1
            return count
        return count_bits(diff)

