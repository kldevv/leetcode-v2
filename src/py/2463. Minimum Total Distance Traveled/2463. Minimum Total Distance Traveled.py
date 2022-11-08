class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        @lru_cache(None)
        def dp(i, j, k):
            # i i robot, given i' is processed where i' > i
            # j j factory
            # k already fix k robot
            if i == len(robot):
                return 0
            if j == len(factory):
                return inf
            
            not_process = dp(i, j+1, 0)
            process = dp(i+1, j, k+1) + abs(robot[i]-factory[j][0]) if factory[j][1] > k else inf
            return min(not_process, process)
        
        return dp(0, 0, 0)

