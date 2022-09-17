class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        out = 0
        for n in range(32):
            mask = 1 << n
            set_one = sum([1 for num in nums if num & mask])
            out += (len(nums) - set_one) * set_one
        return out

