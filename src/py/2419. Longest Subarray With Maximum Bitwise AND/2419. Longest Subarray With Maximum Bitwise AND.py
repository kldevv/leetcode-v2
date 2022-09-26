class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cur_len = 1
        max_len = 1
        max_val = max(nums)
        for i in range(1, n):
            extension_val = nums[i] & nums[i-1]
            if extension_val >= max_val:
                cur_len += 1
                max_val = extension_val
                max_len = max(max_len,  cur_len)
            else:
                cur_len = 1
        return max_len

