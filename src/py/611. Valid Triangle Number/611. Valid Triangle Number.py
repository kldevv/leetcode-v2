class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        out = 0
        for i in range(n):
            long = nums[i]
            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] <= long:
                    k -= 1
                else:
                    out += k - j
                    j += 1
        return out
    