class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def dfs(nums, cur, i):
            nonlocal out
            if i == len(nums):
                out.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(nums, cur, i+1)
            cur.pop()
            dfs(nums, cur, i+1)
        dfs(nums, [], 0)
        return out