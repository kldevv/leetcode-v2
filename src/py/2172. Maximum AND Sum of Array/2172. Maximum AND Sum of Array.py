class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        BASE = 3
        
        @lru_cache(None)
        def dp(i, mask):
            if i == len(nums):
                return 0
            
            out = 0
            for slot in range(1, numSlots+1):
                position = BASE ** (slot - 1)
                if mask // position % BASE:
                    out = max(out, (nums[i]&slot) + dp(i+1, mask-position))
            return out
        
        return dp(0, BASE ** numSlots - 1)