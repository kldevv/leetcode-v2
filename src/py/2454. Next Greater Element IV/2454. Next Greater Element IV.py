class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk1 = []
        stk2 = []
        out = [-1] * n
        for i, num in enumerate(nums):
            while stk2 and nums[stk2[-1]] < num:
                out[stk2.pop()] = num
            temp = []
            while stk1 and nums[stk1[-1]] < num:
                temp.append(stk1.pop())
            stk2 += temp[::-1]
            stk1.append(i)
        return out