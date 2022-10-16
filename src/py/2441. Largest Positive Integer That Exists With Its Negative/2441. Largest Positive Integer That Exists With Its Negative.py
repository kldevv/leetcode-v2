class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        out = -1
        for num in nums:
            if num in seen:
                out = max(out, abs(num))
            seen.add(-num)
        return out
        