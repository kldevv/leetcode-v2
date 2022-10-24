class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        @lru_cache(None)
        def count_cost(x):
            out = 0
            for i, num in enumerate(nums):
                out += abs(num-x) * cost[i]
            return out
        
        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            c, c_next = count_cost(m), count_cost(m+1)
            if c < c_next:
                r = m
            else:
                l = m + 1
        return count_cost(l)

