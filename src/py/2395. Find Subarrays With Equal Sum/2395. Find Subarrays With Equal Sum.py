class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        # fixed-size sliding window
        # keep the sum in the window
        
        required_len = 2
        
        cur_sum = 0
        all_sums = set()
        for i, num in enumerate(nums):
            cur_sum += num
            if i >= required_len:
                cur_sum -= nums[i - required_len]
            
            if i >= required_len - 1:
                if cur_sum in all_sums:
                    return True
                all_sums.add(cur_sum)
        
        return False
            