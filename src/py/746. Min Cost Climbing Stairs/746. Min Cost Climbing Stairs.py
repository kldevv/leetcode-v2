class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one_step_away = 0
        two_step_away = 0
        for i in range(2, len(cost) + 1):
            one_step_away, two_step_away = min(one_step_away + cost[i-1], two_step_away + cost[i-2]), one_step_away
            
        return one_step_away

