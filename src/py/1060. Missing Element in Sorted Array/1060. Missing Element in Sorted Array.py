class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # count the elements missing as iterating thru the array
        n = len(nums)
        for i in range(1, n):
            gap = nums[i] - nums[i-1] - 1
            if gap:
                if gap >= k:
                    return nums[i-1] + k
                else:
                    k -= gap
        return nums[-1] + k
