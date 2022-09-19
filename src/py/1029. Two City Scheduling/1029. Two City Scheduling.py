class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff_a_b = [(cost_a - cost_b, idx)  for idx, (cost_a, cost_b) in enumerate(costs)]
        diff_a_b.sort()
        
        n = len(costs)
        out = 0
        for i in range(n):
            if i < n // 2:
                out += costs[diff_a_b[i][1]][0]
            else:
                out += costs[diff_a_b[i][1]][1]
        return out

