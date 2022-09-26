class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nlogn
        # dynamically build subsequence
        
        sub = [nums[0]]
        for num in nums[1:]:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)