class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # tc(n): O(2^n * n)
        # 2^n bit mask states, each state takes O(n)
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False
        
        n = len(matchsticks)
        side_len = sum(matchsticks) // 4
        
        @lru_cache(None)
        def dfs(used, total):
            # we have match 3 sides
            if total // side_len == 3:
                return True
            
            side_rem = side_len - (total % side_len)
            for i in range(n):
                # if the current match is not used
                # and the current match can fit in the current side
                if not (used & (1 << i)) and matchsticks[i] <= side_rem:
                    # try this match
                    if dfs(used | (1 << i), total + matchsticks[i]):
                        return True
            return False
        
        return dfs(0, 0)

