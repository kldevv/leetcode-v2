class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        max_cost = 0
        out = 0
        for i in range(len(colors)):
            # if the colors are not the same, reset max_cost
            if i > 0 and colors[i] != colors[i-1]:
                max_cost = 0
            # disgard the ballon with the less cost
            out += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        return out