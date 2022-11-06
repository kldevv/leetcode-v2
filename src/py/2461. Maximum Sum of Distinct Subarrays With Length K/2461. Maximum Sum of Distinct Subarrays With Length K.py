class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        cur_sum = 0
        j = 0
        
        cnt = Counter()
        unique = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            cnt[nums[i]] += 1
            unique += cnt[nums[i]] == 1
            if i - j + 1 > k:
                cnt[nums[j]] -= 1
                unique -= cnt[nums[j]] == 0
                cur_sum -= nums[j]
                j += 1
            if unique == k:
                max_sum = max(cur_sum, max_sum)
        return max_sum

