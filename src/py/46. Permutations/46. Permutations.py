class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        
        def backtrack(i):
            if i == n:
                out.append(nums.copy())
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        
        backtrack(0)
        return out