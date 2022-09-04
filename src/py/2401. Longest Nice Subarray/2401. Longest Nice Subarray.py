class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # sliding windows
        
        # keep all the set bits in the subarray
        # newly introduced number needs to have no overlap with all the set bits in the subarray
        all_set_bits = 0
        
        max_len = 0
        j = 0
        for i in range(len(nums)):
            while j < i and all_set_bits & nums[i] != 0:
                all_set_bits ^= nums[j]    
                j += 1    
            max_len = max(max_len, i - j + 1)
            all_set_bits ^= nums[i]
        
        return max_len

