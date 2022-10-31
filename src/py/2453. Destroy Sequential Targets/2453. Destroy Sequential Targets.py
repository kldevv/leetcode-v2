class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        mod = Counter(num % space for num in nums)
        return max(nums, key=lambda x: (mod[x%space], -x))