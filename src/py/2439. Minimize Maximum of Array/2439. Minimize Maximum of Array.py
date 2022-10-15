class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total = nums[0]
        out = nums[0]
        for i in range(1, len(nums)):
            total += nums[i]
            out = max(out, total // (i + 1) + int(total % (i+1) != 0))
        return out