class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        left_small = [nums[0]] * n
        
        for i in range(1, n):
            left_small[i] = min(nums[i], left_small[i-1])
        
        right_medium = []
        for i in range(n-1, -1, -1):
            if nums[i] <= left_small[i]:
                continue
            while right_medium and right_medium[-1] <= left_small[i]:
                right_medium.pop()
            if right_medium and nums[i] > right_medium[-1]:
                return True
            right_medium.append(nums[i])
        return False
        