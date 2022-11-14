class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        tl_cnt = Counter()
        after_cnt = Counter(nums)
        
        for num in nums:
            if tl_cnt[num-1]:
                tl_cnt[num-1] -= 1
                tl_cnt[num] += 1
            elif after_cnt[num+1] > 0 and after_cnt[num+2] > 0:
                after_cnt[num+1] -= 1
                after_cnt[num+2] -= 1
                tl_cnt[num] += 1
            else:
                return False
            after_cnt[num] -= 1
        return True
