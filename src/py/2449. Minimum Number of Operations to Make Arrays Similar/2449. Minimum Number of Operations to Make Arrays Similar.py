class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        sort_func = lambda x: (x & 1, x)
        nums.sort(key=sort_func)
        target.sort(key=sort_func)
        return sum(abs(x-y) for x, y in zip(nums, target)) // 4

