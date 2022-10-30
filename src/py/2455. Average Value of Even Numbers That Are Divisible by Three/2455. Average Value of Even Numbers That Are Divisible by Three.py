class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 6 == 0]
        return sum(nums) // (len(nums) or 1)