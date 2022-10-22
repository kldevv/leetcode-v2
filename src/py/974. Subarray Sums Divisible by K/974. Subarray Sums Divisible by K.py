class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        same_mod_cnt = [1] + [0] * k
        prefix_sum_mod = 0
        out = 0
        for num in nums:
            prefix_sum_mod = (num + prefix_sum_mod) % k
            out += same_mod_cnt[prefix_sum_mod]
            same_mod_cnt[prefix_sum_mod] += 1
        
        return out

