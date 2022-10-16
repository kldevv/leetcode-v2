class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cur_max_idx = 0
        cur_min_idx = 0
        
        j = 0
        out = 0
        for i in range(len(nums)):
            if nums[i] >= nums[cur_max_idx]:
                cur_max_idx = i
            if nums[i] <= nums[cur_min_idx]:
                cur_min_idx = i
            if nums[cur_max_idx] > maxK or nums[cur_min_idx] < minK:
                cur_max_idx = cur_min_idx = j = i
            if nums[cur_max_idx] == maxK and nums[cur_min_idx] == minK:
                out += min(cur_max_idx, cur_min_idx) - j + 1
        return out