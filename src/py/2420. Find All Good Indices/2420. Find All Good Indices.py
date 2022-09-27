class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        max_num = max(nums) + 1
        n = len(nums)
        
        # scan from left
        cur_k = 1
        for i in range(1, n):
            if cur_k >= k:
                nums[i] += max_num
            if (nums[i] % max_num) <= (nums[i-1] % max_num):
                cur_k += 1
            else:
                cur_k = 1
        
        # scan from right
        cur_k = 1
        for i in range(n-2, -1, -1):
            if cur_k >= k:
                nums[i] += max_num
            if (nums[i] % max_num) <= (nums[i+1] % max_num):
                cur_k += 1
            else:
                cur_k = 1
                
        # only return index if valid both from left and right
        return [i for i, num in enumerate(nums) if (num // max_num) == 2]

