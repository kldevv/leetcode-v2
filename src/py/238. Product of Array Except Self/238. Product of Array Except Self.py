class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        
        cur_mul = 1
        for i in range(n):
            out[i] *= cur_mul
            cur_mul *= nums[i]
        cur_mul = 1
        for i in range(n-1, -1, -1):
            out[i] *= cur_mul
            cur_mul *= nums[i]
        
        return out
            