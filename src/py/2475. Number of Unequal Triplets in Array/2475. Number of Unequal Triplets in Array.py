class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cnt = Counter()
        out = 0
        
        cnt_pair = 0
        
        for i in range(len(nums)):
            # triple contains nums[i] == all unique pairs without nums[i]
            # all unique pairs without nums[i] = all unique pairs - unique pairs before i with nums[i]
            out += cnt_pair - cnt[nums[i]] * (i - cnt[nums[i]])
            cnt_pair += i - cnt[nums[i]]
            cnt[nums[i]] += 1
        return out
